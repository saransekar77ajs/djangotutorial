from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view),
    path("movies_list/", views.movies_list),
    path("movie/<int:id>/", views.movie_detail, name="movie_detail"),
    path("api/movie/", views.movie_json),
]
