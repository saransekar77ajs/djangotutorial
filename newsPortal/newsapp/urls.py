from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("news/<str:category>/", views.news_list, name="news_by_category"),
]
