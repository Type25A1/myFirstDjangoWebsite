from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'MO',
    'title': 'Blog Post 1',
    'content': 'first post content',
    'date_posted': 'august 27, 2020'
    },
    {
    'author': 'MOf',
    'title': 'Blog ost 2',
    'content': 'first post cofdsfdntent',
    'date_posted': 'august 27, 2090'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
