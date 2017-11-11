from django.shortcuts import render
from pinax.blog.views import BlogIndexView


class IndexView(BlogIndexView):
	template_name = 'index.html'
	pass