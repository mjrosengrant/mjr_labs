from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from models import Post



# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-pub_date')
    template = loader.get_template('blog/index.html')
    context = {
        'post_list': post_list,
    }
    return HttpResponse(template.render(context, request))