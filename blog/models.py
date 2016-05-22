from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse

from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = HTMLField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
	    return reverse('blog:view_blog_post',kwargs={"slug":self.slug})

class WordPressPost(Post):
    pass

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
    	return reverse('blog:view_blog_category',kwargs={"slug":self.slug})
