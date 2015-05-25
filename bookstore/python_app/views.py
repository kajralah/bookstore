from django.contrib import auth
from django.http import HttpResponseRedirect
from bookstore.python_app.py.User import *
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from bookstore.python_app.py.DBController import *


class IndexView(TemplateView):
    template_name = 'index.html'

@csrf_exempt
def login(request):
    db = DBController()
    username = request.POST.get('name','default')
    password = request.POST.get('password','default')
    check = request.POST.get('check','default')
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken','default')
    if db.return_existing_user(username,password) is None:
    	return HttpResponse('Error login')
    else:
        request.session['user_id'] =db.get_user_id(username,password)
        return HttpResponse('Welcome')

@csrf_exempt
def register(request):
    db = DBController()
    username = request.POST.get('username','default')
    password = request.POST.get('password','default')
    address = request.POST.get('address','default')
    phone = request.POST.get('phone','0000000000')
    email = request.POST.get('email','default@default.com')
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken','default')
    if User.is_password_correct(password) is False:
        return HttpResponse('Wrong password')
    else:
        try:
            db.add_user_to_db(username,password,address,phone,email,'F')
            return HttpResponse('Registration complete')
        except ExistingUserException:
            return HttpResponse('User exists')
            
def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")