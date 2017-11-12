"""Urls for mjrosengrant.com."""

from django.conf.urls import url
from mjrosengrant_com import views

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$",
        views.PostView.as_view(), name="post"),
]
