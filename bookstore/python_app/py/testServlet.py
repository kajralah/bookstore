from django.contrib import auth
from django.http import HttpResponseRedirect
from User.py import *

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if User.validating_login(username,password) is True:
    	return True
    else 
    	return False