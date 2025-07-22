from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "release_year": 1994,
        "description": "Two imprisoned men bond over the years, finding redemption through acts of common decency.",
        "rating": 9.3,
        "poster": "https://m.media-amazon.com/images/I/51NiGlapXlL._AC_.jpg",
    },
    {
        "id": 2,
        "title": "The Godfather",
        "release_year": 1972,
        "description": "The aging patriarch of an organized crime dynasty transfers control to his reluctant son.",
        "rating": 9.2,
        "poster": "https://static1.srcdn.com/wordpress/wp-content/uploads/2023/05/the-godfather-poster.jpeg",
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "release_year": 2008,
        "description": "Batman faces the Joker, a criminal mastermind who pushes Gotham into chaos.",
        "rating": 9.0,
        "poster": "https://www.themoviedb.org/t/p/original/eP5NL7ZlGoW9tE9qnCdHpOLH1Ke.jpg",
    },
    {
        "id": 4,
        "title": "Pulp Fiction",
        "release_year": 1994,
        "description": "The lives of two mob hitmen, a boxer, and others intertwine in tales of violence and redemption.",
        "rating": 8.9,
        "poster": "https://alternativemovieposters.com/wp-content/uploads/2021/04/RuizBurgos_PulpFiction.jpg",
    },
    {
        "id": 5,
        "title": "Forrest Gump",
        "release_year": 1994,
        "description": "Forrest Gump, a man with a low IQ, lives an extraordinary life and influences major historical events.",
        "rating": 8.8,
        "poster": "https://cdn11.bigcommerce.com/s-yzgoj/images/stencil/1280x1280/products/2928612/5938074/MOVCJ2095__34631.1679584529.jpg?c=2",
    },
    {
        "id": 6,
        "title": "Inception",
        "release_year": 2010,
        "description": "A thief who enters people's dreams is given a task to plant an idea instead of stealing it.",
        "rating": 8.8,
        "poster": "https://cdn.shopify.com/s/files/1/1416/8662/products/inception_2010_imax_original_film_art_2000x.jpg?v=1551890318",
    },
    {
        "id": 7,
        "title": "Fight Club",
        "release_year": 1999,
        "description": "An office worker and a soap maker form an underground fight club that evolves into something much more.",
        "rating": 8.8,
        "poster": "https://m.media-amazon.com/images/I/51v5ZpFyaFL._AC_.jpg",
    },
    {
        "id": 8,
        "title": "Interstellar",
        "release_year": 2014,
        "description": "A team of explorers travel through a wormhole in space in an attempt to save humanity.",
        "rating": 8.6,
        "poster": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/297acd129204217.616629e21fe76.png",
    },
    {
        "id": 9,
        "title": "The Matrix",
        "release_year": 1999,
        "description": "A hacker discovers the nature of reality and joins a rebellion against its controllers.",
        "rating": 8.7,
        "poster": "https://m.media-amazon.com/images/I/51vpnbwFHrL._AC_.jpg",
    },
    {
        "id": 10,
        "title": "Gladiator",
        "release_year": 2000,
        "description": "A former Roman general seeks revenge against the corrupt emperor who murdered his family.",
        "rating": 8.5,
        "poster": "https://i.pinimg.com/736x/32/5a/d8/325ad832426c9dc0eedb8bf8853897c4.jpg",
    },
]


def home_view(request):
    return HttpResponse("<h1> Movie Gallery Home Page. </h1>")


def movies_list(request):
    context = {"movies": movies}
    return render(request, "movies/home.html", context)


def movie_detail(request, id):
    movie = next((m for m in movies if m["id"] == id), None)
    if movie:
        return render(request, "movies/movie_detail.html", {"movie": movie})
    else:
        return HttpResponse("<h2>Movie not found</h2>", status=404)


def movie_json(request):
    return JsonResponse(movies, safe=False)
