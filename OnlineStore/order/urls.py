from django.urls import path, include
from . import views

urlpatterns = [
    path("place_order/", views.place_order, name="placeOrder"),
    path("order_history/", views.order_history, name="orderHistory"),
]
