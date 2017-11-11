from django.conf.urls import url
from mjrosengrant_com import views

urlpatterns = [
    url(r"", views.IndexView.as_view(), name="blog"),
]