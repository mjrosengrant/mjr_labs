"""mjrlabs URL Configuration
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('mjrosengrant_com.urls')),
    url(r'^pinax-blog/', include('pinax.blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
