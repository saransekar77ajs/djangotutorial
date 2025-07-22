from django.urls import path
from . import views

urlpatterns = [
    path("product_list", views.product_list, name="productList"),
    path("product_detail/<int:prod_id>", views.product_detail, name="productDetail"),
]
