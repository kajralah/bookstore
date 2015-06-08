from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate
from bookstore.python_app.py.DBController import *


class IndexView(TemplateView):
    template_name = 'index.html'


@csrf_exempt
def login(request):
    db = DBController()
    username = request.POST.get('name', 'default')
    password = request.POST.get('password', 'default')
    check = request.POST.get('check', 'default')
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', 'default')
    if db.return_existing_user(username, password) is None:
        return HttpResponse('Error login')
    elif db.return_existing_user(username, password).username == 'ADMIN':
        request.session['user_id'] = db.get_user_id(username, password)
        return HttpResponse('ADMIN')
    else:
        request.session['user_id'] = db.get_user_id(username, password)
        return HttpResponse('Welcome')


@csrf_exempt
def register(request):
    db = DBController()
    username = request.POST.get('username', 'default')
    password = request.POST.get('password', 'default')
    address = request.POST.get('address', 'default')
    phone = request.POST.get('phone', '0000000000')
    email = request.POST.get('email', 'default@default.com')
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', 'default')
    if User.is_password_correct(password) is False:
        return HttpResponse('Wrong password')
    else:
        try:
            db.add_user_to_db(username, password, address, phone, email, 'F')
            return HttpResponse('Registration complete')
        except ExistingUserException:
            return HttpResponse('User exists')

@csrf_exempt
def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        return HttpResponse("You're not logged in")
    return HttpResponse("You're logged out.")

@csrf_exempt
def profile(request):
    db = DBController()
    user_id = request.session['user_id']
    user = db.return_user_by_id(user_id)
    if user is None:
        return HttpResponse("You're not logged in")
    else:
        return HttpResponse(user.email+','+user.address+','+user.phone)

@csrf_exempt
def num_of_liked_products(request):
    db=DBController()
    user_id = request.session['user_id']
    user = db.return_user_by_id(user_id)
    if user is None:
        return HttpResponse("You're not logged in")
    else:
        number_of_liked_product = db.number_of_liked_product(user_id)
        number_of_bougth_product = db.number_of_bought_items(user_id)
        result = str(number_of_liked_product)+','+str(number_of_bougth_product)
        return HttpResponse(result)
