from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index),

	url(r'^post/(?P<slug>[^\.]+)', 
	    views.view_post, 
	    name='view_blog_post'
    ),

	url(r'^category/(?P<slug>[^\.]+)', 
		views.view_category, 
	    name='view_blog_category'
    ),

]