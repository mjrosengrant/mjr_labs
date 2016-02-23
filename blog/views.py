from django.http import HttpResponse
from django.template import loader

from models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.

def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()
    })

def view_post(request, slug):   
    return render_to_response('blog/view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })

def view_portfolio(request):
    return render_to_response('blog/portfolio.html')

def add_post(request):
    return render_to_response('blog/wysiwyg.html')