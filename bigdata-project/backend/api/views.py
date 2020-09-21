from api import models, serializers
from rest_framework import viewsets
from .models import Star, Genre_Webtoon, Webtoon, Wish, Genre, Ranking
# post 요청
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, mixins
# 필터
import django_filters.rest_framework
from rest_framework import filters
# 예외처리
from rest_framework.exceptions import NotAuthenticated, NotFound, ValidationError
# 유저 모델
from accounts.models import User


# 페이지네이션
class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


# 랭킹
class RankingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RankingSerializer
    queryset = Ranking.objects.all().order_by("id")

    # distinct로 필터
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['distinct']


# 웹툰
class WebtoonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WebtoonSerializer
    pagination_class = SmallPagination
    queryset = Webtoon.objects.all()

    # 키워드 검색
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title', 'artists_rels__name'] # 작품이름, 작가이름 

    # 장르로 필터
    filterset_fields = ['genres_rels__name', 'distinct']

    # 웹툰의 전체 평점,댓글 목록
    @action(methods=['GET'], detail=True, url_path="ratings")
    def webtoon_ratings(self, request, *args, **kwargs):
        webtoon = self.get_object()
        serializer_class = serializers.StarUserSerializer
        queryset = Star.objects.filter(webtoon=webtoon)
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


    # 평점매기기
    @action(methods=['GET', 'POST', 'PUT', 'DELETE'], detail=True, url_path="stars")
    def webtoon_star(self, request, *args, **kwargs):
        webtoon = self.get_object()
        serializer_class = serializers.StarUserSerializer
        user = request.user
        
        # 유저 평점에 관련된 부분이므로 로그인 되어있어야
        if request.user.is_anonymous:
            raise NotAuthenticated("로그인 먼저 해주세요")
        else:
            # 해당 유저의 평가 기록
            user_rating = Star.objects.filter(user=user, webtoon=webtoon)
            
            if request.method == 'GET':
                serializer = serializer_class(user_rating, many=True)
                return Response(serializer.data)

            elif request.method == 'POST':
                if user_rating: # 프론트에서 해결 가능
                    raise ValidationError('이미 평가하였습니다.')

                elif 1 <= request.data.get('rating') <= 10:
                    Star(user=user, webtoon=webtoon, rating=request.data.get('rating'), content="").save()
                    user_rated = Star.objects.filter(user=user, webtoon=webtoon)
                    serializer = serializer_class(user_rated, many=True)
                    return Response(serializer.data)

                raise ValidationError('잘못된 값이 입력되었습니다.')

            elif request.method == 'PUT':
                if user_rating is None: # 프론트에서 해결 가능
                    raise NotFound("평가하지 않은 웹툰입니다.")

                elif 1 <= request.data.get('rating') <= 10:
                    if request.data.get('content'):
                        user_rating.first().content = request.data.get('content')
                    if request.data.get('rating'):
                        user_rating.first().rating = request.data.get('rating')
                    
                    user_rating.first().save()
                    serializer = serializer_class(user_rating, many=True)
                    return Response(serializer.data)

                raise ValidationError('잘못된 값이 입력되었습니다.')
            
            elif request.method == 'DELETE':
                if user_rating is None:
                    raise NotFound("평가하지 않은 웹툰입니다.")
                else:
                    user_rating.first().delete()
                    return Response({'result': 'deleted'})


    # 보고싶어요
    @action(methods=['GET', 'POST', 'DELETE'], detail=True, url_path="wishes")
    def webtoon_wish(self, request, *args, **kwargs):
        webtoon = self.get_object()
        serializer_class = serializers.WishSerializer
        user = request.user
        
        # 유저 보고싶어요에 관련된 부분이므로 로그인 되어있어야
        if request.user.is_anonymous:
            raise NotAuthenticated("로그인 먼저 해주세요")
        else:
            # 해당 유저의 보고싶어요 여부
            user_wishes = Wish.objects.filter(user=user, webtoon=webtoon)
            
            if request.method == 'GET':
                serializer = serializer_class(user_wishes, many=True)
                return Response(serializer.data)

            elif request.method == 'POST':
                if user_wishes: # 프론트에서 해결 가능
                    raise ValidationError('이미 보고싶어요 하였습니다.')
                else:
                    Wish(user=user, webtoon=webtoon).save()
                    user_wished = Wish.objects.filter(user=user, webtoon=webtoon)
                    serializer = serializer_class(user_wished, many=True)
                    return Response(serializer.data)

                raise ValidationError('잘못된 값이 입력되었습니다.')
            
            elif request.method == 'DELETE':
                if user_wishes is None:
                    raise NotFound("보고싶어요 하지 않은 웹툰입니다.")
                else:
                    user_wishes.first().delete()
                    return Response({'result': 'deleted'})


# 유저정보
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    # 유저가 평가한 웹툰 목록
    @action(methods=['GET'], detail=True, url_path="stars")
    def user_star(self, request, *args, **kwargs):
        user = self.get_object()
        serializer_class = serializers.StarWebtoonSerializer
        user_stared = Star.objects.filter(user=user)
        serializer = serializer_class(user_stared, many=True)
        return Response(serializer.data)

    # 유저가 보고싶어요한 웹툰 목록
    @action(methods=['GET'], detail=True, url_path="wishes")
    def user_wish(self, request, *args, **kwargs):
        user = self.get_object()
        serializer_class = serializers.WishWebtoonSerializer
        user_wished = Wish.objects.filter(user=user)
        serializer = serializer_class(user_wished, many=True)
        return Response(serializer.data)


# 장르
class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.GenreSerializer
    queryset = Genre.objects.all().order_by("id")


# 장르
class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GenreSerializer
    def get_queryset(self):
        queryset = (
            models.Genre.objects.all().order_by("id")
        )
        return queryset


# 나중에 전부 get_object_or_404(queryset, pk=pk) 형식으로 바꿔야될듯
# class SmallPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = "page_size"
#     max_page_size = 50


# class StoreViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.StoreSerializer
#     pagination_class = SmallPagination

#     def get_queryset(self):
#         name = self.request.query_params.get("name", "")
#         queryset = (
#             models.Store.objects.all().filter(store_name__contains=name).order_by("id")
#         )
#         return queryset

# class ReivewViewset(viewsets.ModelViewSet):
#     serializer_class = serializers.ReviewSerializer

#     def get_queryset(self):
#         # name = self.request.query_params.get("name","")
#         store = self.request.query_params.get("store")
#         queryset = (
#             models.Review.objects.all().filter(store=store).order_by("id")
#         )
#         return queryset

# class ReviewPost(viewsets.ModelViewSet):
#     serializer_class = serializers.ReviewSerializer
#     @action(detail=True, methods=['post'])
#     def post_review(self, request):
#         # if serializer.is_valid(raise_exception=True):
#         serializer_class.save()
#         return Response(serializer_class.data)


# class DetailStore(viewsets.ModelViewSet):
#     serializer_class = serializers.StoreSerializer

#     def get_queryset(self):
#         store_id = self.request.query_params.get("store_id")
#         queryset = (
#             models.Store.objects.all().filter(id=store_id).order_by("id")
#         )
#         return queryset


