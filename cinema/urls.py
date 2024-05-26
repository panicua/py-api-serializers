from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"
router = DefaultRouter()

router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet, basename="genre")
router.register("actors", ActorViewSet, basename="actor")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register(
    "movie_sessions", MovieSessionViewSet, basename="movie_session"
)

urlpatterns = [
    path("", include(router.urls)),
]
