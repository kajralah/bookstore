from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate
from bookstore.python_app.py.DBController import *
from bookstore.python_app.py.Book import *
from bookstore.python_app.py.User import *
from io import BytesIO
from PIL import Image
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse

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
            db.add_user_to_db(username, password, address, phone, email)
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
def isLoggedUser(request):
    try:
        user_id = request.session['user_id']
        return HttpResponse(user_id)
    except KeyError:
        return HttpResponse('False')


@csrf_exempt
def profile(request):
    db = DBController()
    try:
        user_id = request.session['user_id']
        user = db.return_user_by_id(user_id)
        if user is None:
            return HttpResponse("You're not logged in")
        else:
            return HttpResponse(user.email+','+user.address+','+user.phone)
    except KeyError:
        return HttpResponse("You're not logged in")


@csrf_exempt
def num_of_liked_products(request):
    db=DBController()
    try:
        user_id = request.session['user_id']
        user = db.return_user_by_id(user_id)
        if user is None:
            return HttpResponse("You're not logged in")
        else:
            number_of_liked_product = db.number_of_liked_product(user_id)
            number_of_bougth_product = db.number_of_bought_items(user_id)
            result = str(number_of_liked_product)+','+str(number_of_bougth_product)
            return HttpResponse(result)
    except KeyError:
        return HttpResponse("You're not logged in")


@csrf_exempt
def add_book(request):
    title = request.POST['name-input']
    price = request.POST['price-input']
    description = request.POST['desc-input']
    author = request.POST['author-input']
    pages = request.POST['pages-input']
    publisher = request.POST['publisher-input']
    category = request.POST['category-input']
    image = request.FILES.get['myfile',None]
    
    image_name = title
    image_folder = 'bookstore\python_app\static\img'
    image_extension = '.jpg'

    destination = open(image_folder+'\\'+image_name+image_extension, 'wb+')
    for chunk in image.chunks():
        destination.write(chunk)
    destination.close()

    db = DBController()
    db.add_book_to_db(title,price,author,pages,image_name+image_extension,
        publisher,description,db.get_category_id_by_name(category))

    return HttpResponseRedirect('index.html') 


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
    title = request.POST['title']
    db=DBController()
    book_id = db.get_book_id_by_title(title)
    book = db.get_book_by_id(book_id)
    list_of_book =[book.book_title,book.book_price,book.book_author,book.book_pages]
    list_of_description = [book.book_publisher,book.book_description,
    db.get_categorie_by_id(book.book_category),book.book_image]
    list_of_book.extend(list_of_description)
    list_of_book_description = [str(book_element) + "," for book_element in list_of_book]
    return HttpResponse(list_of_book_description)

@csrf_exempt
def like_book(request):
    db = DBController()
    try:
        user_id = request.session['user_id']
        category_name = request.POST['category']
        book_title = request.POST['title']
        db.insert_into_user_liked_books(user_id,book_title)
        db.insert_into_liked_categories(user_id,category_name)
        return HttpResponse('True')
    except (cx_Oracle.IntegrityError,KeyError):
        HttpResponse('False')

@csrf_exempt
def buy_book(request):
    db=DBController()
    try:
        user_id = request.session['user_id']
        book_title = request.POST['title']
        db.insert_into_user_bought(user_id,book_title)
        return HttpResponse('True')
    except (cx_Oracle.IntegrityError,KeyError):
        return HttpResponse('False')


@csrf_exempt
def is_supervisor(request):
    db = DBController()
    try:
        user_id = request.session['user_id']
        is_supervisor = db.is_supervisor(user_id)
        return HttpResponse(is_supervisor)
    except KeyError:
        return HttpResponse('False')

@csrf_exempt
def changeProfile(request):
    db=DBController()
    try:
        user_id = request.session['user_id']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['password']
        repeated_pass = request.POST['password2']
        result = User.is_password_correct(password)
        if password != repeated_pass:
            return HttpResponse('Password don\'t match')
        db.change_user(user_id,password,email,address,phone)
        return HttpResponseRedirect('index.html')
    except IncorrectPasswordException:
        return HttpResponse('Incorrect Password')
    except KeyError:
        return HttpResponseRedirect('index.html')


@csrf_exempt
def boughtBooks(request):
    db=DBController()
    try:
        user_id = request.session['user_id']
        list_of_books = db.show_bought_books_by_user(user_id)
        return HttpResponse(list_of_books)
    except KeyError:
        return HttpResponseRedirect('index.html')
