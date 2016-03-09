from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

__author__ = 'max ma'

urlpatterns = [
    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

