"""mjrlabs URL Configuration."""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('mjrosengrant_com.urls', namespace='mjrosengrant_com')),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('pinax.blog.urls', namespace='pinax-blog')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
