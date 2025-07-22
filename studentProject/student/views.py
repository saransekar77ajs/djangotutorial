from django.shortcuts import render


def student_data(request):
    context = {
        "student_profile": [
            {
                "name": "John Doe",
                "age": 24,
                "course": "Python Full Stack Developer",
                "email": "john@example.com",
                "image": "https://randomuser.me/api/portraits/men/1.jpg",
            },
            {
                "name": "Sarah Hill",
                "age": 27,
                "course": "React JS",
                "email": "sarah@example.com",
                "image": "https://randomuser.me/api/portraits/women/2.jpg",
            },
            {
                "name": "Sally Smith",
                "age": 25,
                "course": "Front End Developer",
                "email": "sally@example.com",
                "image": "https://randomuser.me/api/portraits/women/3.jpg",
            },
            {
                "name": "David Fox",
                "age": 28,
                "course": "Data Science",
                "email": "david@example.com",
                "image": "https://randomuser.me/api/portraits/men/4.jpg",
            },
            {
                "name": "Peter Parker",
                "age": 23,
                "course": "Machine Learning",
                "email": "peter@example.com",
                "image": "https://randomuser.me/api/portraits/men/5.jpg",
            },
        ]
    }

    return render(request, "student/index.html", context)
