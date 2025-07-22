from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def profile(request):
    context = {
        "customer_profile": [
            {
                "name": "Sally Smith",
                "membership": "Platinum",
                "email": "salsmith@email.com",
            },
            {
                "name": "Peter Parker",
                "membership": "Bronze",
                "email": "petepark@email.com",
            },
            {
                "name": "John Doe",
                "membership": "Gold",
                "email": "johndoe@email.com",
            },
        ]
    }
    return JsonResponse(context)


def dashboard(request):
    customer_dashboard = """
    <h1>Welcome to Customer Dashboard! </h1> 
    """
    return HttpResponse(customer_dashboard)
