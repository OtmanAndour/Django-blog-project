from django.shortcuts import render

posts = [
    {
        'author': 'Otman Andour',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': 'June 22, 2020'

    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 2 ',
        'content': 'Second post content',
        'date': 'June 23, 2020'

    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
