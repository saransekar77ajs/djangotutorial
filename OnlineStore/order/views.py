from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def place_order(request):
    return HttpResponse("<h1>Order Placed Successfully.</h1>")


def order_history(request):
    context = {
        "orders": [
            {"id": 1, "item": "Laptop", "status": "Delivered"},
            {"id": 2, "item": "Mobile", "status": "Pending"},
            {"id": 3, "item": "Air Pod", "status": "Processing"},
        ]
    }
    return JsonResponse(context)
