from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def product_list(request):
    context = {"products": ["Laptop", "Mobile", "Air Pod"]}
    return JsonResponse(context)


def product_detail(request, prod_id):
    details = f"""
            <h2> Product Detail Information for Product ID: {prod_id} </h2>
        """
    return HttpResponse(details)
