from django.shortcuts import render
from pinax.blog.views import BlogIndexView


class IndexView(BlogIndexView):
	template_name = 'mjrosengrant_com/index.html'
	pass