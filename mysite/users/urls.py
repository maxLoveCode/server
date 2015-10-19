__author__ = 'max ma'

from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<users_id>[0-9]+)/add_user$', views.add_user, name='add_user')
]

