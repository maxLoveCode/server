from django.shortcuts import render
from django.http import HttpResponse


from .models import User


def index(request):
    user_list = User.objects.order_by('id')[:5]
    output = ', '.join([p.name for p in user_list])
    return HttpResponse(output)


def add_user(request, users_id):
    return HttpResponse("Adding user for %s" % users_id)
