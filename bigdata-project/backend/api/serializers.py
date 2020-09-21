from .models import Webtoon, Genre, Artist, Artist_Webtoon, Genre_Webtoon, Star, Ranking
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
        ]

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            "id",
            "name",
        ]


class WebtoonSerializer(serializers.ModelSerializer):
    # 조인의 개념
    genres_rels = GenreSerializer(read_only=True, many=True)
    artists_rels = ArtistSerializer(read_only=True, many=True)

    class Meta:
        model = Webtoon
        fields = [
            "id",
            "origin_id",
            "title",
            "description",
            "genres",
            "artists",
            "rating",
            "link",
            "thumb_img",
            "distinct",
            "genres_rels",
            "artists_rels",
        ]


class GenreWebtoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre_Webtoon
        fields = [
            "id",
            "webtoon_id",
            "genre_id",
        ]

class ArtistWebtoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist_Webtoon
        fields = [
            "id",
            "webtoon_id",
            "artist_id",
        ]

class StarUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Star
        fields = [
            "webtoon_id",
            "user",
            "rating",
            "content",
        ]

class StarWebtoonSerializer(serializers.ModelSerializer):
    webtoon = WebtoonSerializer(read_only=True, many=False)
    class Meta:
        model = Star
        fields = [
            "webtoon",
            "user_id",
            "rating",
            "content",
        ]

class WishSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Star
        fields = [
            "webtoon_id",
            "user",
        ]


class WishWebtoonSerializer(serializers.ModelSerializer):
    webtoon = WebtoonSerializer(read_only=True, many=False)
    class Meta:
        model = Star
        fields = [
            "webtoon",
            "user_id",
        ]


class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = [
            "origin_id",
            "distinct",
            "rank",
        ]
