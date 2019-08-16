from django.shortcuts import render
from django.contrib.auth import (login as auth_login,  authenticate)
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return render(request,'app/home.html')
