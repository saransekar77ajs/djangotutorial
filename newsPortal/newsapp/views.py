from django.shortcuts import render
import requests

categories = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology",
]


def home_page(request):
    context = {"categories": categories}
    return render(request, "home.html", context)


def news_list(request, category):
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=91a6213dfe014dbf820e279262ec5361"

    response = requests.get(url)

    news_data = response.json()

    articles = news_data.get("articles", []) if news_data.get("status") == "ok" else []

    context = {"articles": articles, "category": category}

    return render(request, "news.html", context)
