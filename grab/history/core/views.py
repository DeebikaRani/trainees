from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.template.context import RequestContext



# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'home.html')