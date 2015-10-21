from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import User


def index(request):
    user_list = User.objects.order_by('id')[0:10]
    return render(request, 'users/index.html', {'user_list': user_list})


def add_user(request, users_id):
    return HttpResponse("Adding user for %s" % users_id)


def user_detail(request, users_id):
    user = get_object_or_404(User, pk=users_id)
    return render(request, 'users/detail.html', {'user': user})
