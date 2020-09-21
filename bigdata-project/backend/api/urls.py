from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter(trailing_slash=False)
router.register(r"webtoons", views.WebtoonViewSet, basename="webtoons")
router.register(r"rankings", views.RankingViewSet, basename="rankings")
router.register(r"genres", views.GenreViewSet, basename="genres")
router.register(r"users", views.UserViewSet, basename="users")

urlpatterns = router.urls
