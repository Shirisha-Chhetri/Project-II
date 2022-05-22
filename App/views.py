# from http.client import HTTPResponse
import json,re
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404

from .ml import get_recommendation_for_book
from .forms import SignupForm,UploadForm,GenreForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Book,Genre
from django.db import transaction
from django.contrib.auth.models import User
import pandas as pd
from django.contrib.auth.hashers import make_password 

from django.http import JsonResponse


# to show books according to genre
def bookongenre(request):
    genreid = request.GET.get('genre')
    if genreid:
        book = Book.get_book_by_id(genreid).order_by('-id')[:10]
    return render(request, 'booksongenre.html',{'books':book})

# to go to specific book
def specific_book(request,id):
    b = Book.objects.get(id = id)
    specificbook = get_object_or_404(Book, pk=id)
    context = {
            'is_favourite' :False
        }

    if b.wishlist.filter(pk = request.user.pk).exists():
            context['is_favourite']= True
    return render(request,'specific_book.html',{
        'book':specificbook,
        'context':context
        })

# to add books to wishlist
def add_fav(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id = id)
        book.wishlist.add(request.user)
        return redirect('/getbook/{0}'.format(id))          
    else:
        return redirect('/login/')  
   
# to remove books from wishlist
def remove_fav(request,id):
    book = Book.objects.get(id = id)
    book.wishlist.remove(request.user)

    return redirect('/getbook/{0}'.format(id))


# to show added wishlist books on my wishlist href
def get_user_fav(request):
    favbook =request.user.wishlist.all()
    return render(request,'wishlist.html',{'favbook':favbook})

def about(request):
    return render(request,'about.html')


# login module
def loginuser(request):
    if request.method == "POST":
        error_messages={}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user.get_username())
            login(request, user)
            return redirect('/')
        else:
            messages.success(request,"Invalid username or password")
            return redirect('/login/')   
    return render(request,'login.html')

def logouts(request):
    logout(request)
    return redirect('/')

# signup module   
def signup(request):
    error_message = {}
    val={}

    if request.method == "POST":
        fn = request.POST['first_name']
        ln =  request.POST['last_name']
        un =  request.POST['username']
        email = request.POST['email']
        password =  request.POST['password']

        user = User(first_name = fn,
                        last_name = ln,
                        username = un,
                        email = email,
                        password = password)
          
        if(not fn):
            error_message = "Enter firstname"
        elif (fn.isnumeric()):
            error_message = "FirstName cannot be the number"

        elif (not ln):
            error_message = "Enter lastname"
        elif (ln.isnumeric()):
            error_message = "LastName cannot be the number"
        
        elif not un:
            error_message = "Enter username"
        elif (un.isnumeric()):
            error_message = "Username cannot be the number"

        elif not email:
            error_message = "Enter Email"
        elif (email.isnumeric()):
            error_message = "Email cannot be the number"

        elif not password:
            error_message = "Enter Password"
        elif len(password) < 5:
            error_message = "Password must be greater than 5 character"

        elif User.objects.filter(email = email).exists():
            error_message = "Email already registered.."

        elif User.objects.filter(username = un).exists():
            error_message = "Username already registered.."

        if not error_message:
            user.password = make_password(user.password)
            user.save()
            return redirect('/login')
        else:
            return render(request,'register.html',{'error':error_message})
    return render(request,'register.html')

# home module with genre and sliding image
def allgenre(request):
    genre = Genre.objects.all()[0:19]
    slider = Book.objects.all().order_by('id')[:6]
    return render(request, 'home.html',{
        'genres':genre,
        'sliding':slider})

# allgenre.html
def genre(request):
    gen = Genre.objects.all()
    return render(request,'allgenre.html',{'gen':gen})
   
# book module
def allbook(request):
    book = Book.objects.all().order_by('-id')[:72]
    return render(request, 'books.html',{'books':book})

# search module and then recommendation
def search(request):
    if 'search' in request.GET:
        sea = request.GET['search']
        # regex =  r"([a-zA-Z]+) (\d+)"
       
        # s=sea.replace('"','')
        data = Book.objects.filter(title__istartswith=sea)
    
    #for recommendation
    # book_ids = get_recommendation_for_book(id)
    # recommend_book = Book.objects.filter(id__in = book_ids)
    return render(request, 'search.html',{
        'data': data,
        # 'recommended_book': recommend_book
        })
    
   
# autocomplete search module
def search_auto(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        q = request.GET.get('term','')
        bookey = Book.objects.filter(title__istartswith=q)[0:10]
        results = []

        for pl in bookey:
            book_json = {}
            book_json['title'] = pl.title 
            book_json['image'] = pl.image
            results.append(book_json)
       
        data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

# dataset upload form module
def upload(request):
    file_form = UploadForm()
    error_messages = {}

    if request.method == "POST":
        file_form = UploadForm(request.POST, request.FILES)
        try:
            if file_form.is_valid():
            
                dataset = pd.read_csv(request.FILES['uploadfile'])
                new_book_list =[]
                with transaction.atomic():

                    for index, row in dataset.iterrows():
                        book = Book(
                            title = row['title'], 
                            genre = row['genre'],                      
                            description = row['description'],
                            author = row['author'],
                            bookformat = row['bookformat'],
                            isbn = row['isbn'],
                            pages = row['pages'],                           
                            image = row['image']
                        )
                        new_book_list.append(book)
                Book.objects.bulk_create(new_book_list)
                return redirect('/book/page/1')

        except Exception as e:
            print(e)
            error_messages['error'] = e

    return render(request, 'upload_dataset.html',{'form' : file_form,
                                    'error_messages': error_messages})