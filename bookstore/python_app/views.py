from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate
from bookstore.python_app.py.DBController import *
from bookstore.python_app.py.Book import *
from io import BytesIO
from PIL import Image
from django.shortcuts import render_to_response

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

#@csrf_exempt
#def index(request):
#    if request is not None:
#        if request.session['user_id'] is not None:
#            user_id = request.session['user_id']
#            db = DBController()
#            user = db.return_user_by_id(user_id)
#            if user.username == 'ADMIN':
#                return HttpResponse('ADMIN')
#            else :
#                return HttpResponse('Welcome')
#    else: 
#        HttpResponse('None')

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

#category should be entered
@csrf_exempt
def add_book(request):
    title = request.POST['name-input']
    price = request.POST['price-input']
    description = request.POST['desc-input']
    author = request.POST['author-input']
    pages = request.POST['pages-input']
    publisher = request.POST['publisher-input']
    image = request.FILES['myfile']
    
    image_name = title
    image_folder = 'bookstore\python_app\static\img'
    image_extension = '.jpg'

    destination = open(image_folder+'\\'+image_name+image_extension, 'wb+')
    for chunk in image.chunks():
        destination.write(chunk)
    destination.close()

    category = 1
    db = DBController()
    db.add_book_to_db(title,price,author,pages,image_name+image_extension,publisher,description,1)
    return render_to_response('index.html')

@csrf_exempt
def get_categories(request):
    db = DBController()
    list_of_categories = db.get_categories()
    return HttpResponse(list_of_categories)

@csrf_exempt
def show_book(request):
    db=DBController()
    list_of_books = db.show_book()
    return HttpResponse(list_of_books)

@csrf_exempt
def show_product(request):
    name = request.POST['name']
    db=DBController()
    id = db.get_book_id_by_name(name)
    book = db.get_book_by_id(id)
    list_of_book = []

    list_of_book.append(book.book_title)
    
    return HttpResponse(list_of_book)