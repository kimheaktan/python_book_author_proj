from django.shortcuts import render, redirect
from apps.books_authors_app.models import *

def index(request):
    info={
        'books': Book.objects.all(),
    }
    return render(request,"books_authors_app/index.html", info)

def view_book(request, book_id): 
    
    info={
        'book': Book.objects.get(id=book_id),
        'authors' :Author.objects.filter(books__id=book_id),
        'author_drop' : Author.objects.all(),
        # 'book_id': book_id
        # 'description' : Book.objects.get(id=book_id),
    }
    return render(request,'books_authors_app/view_book.html', info )


 
def create_book(request):
    Book.objects.create(title=request.POST["title"],desc=request.POST["description"])
    
    return redirect('/')

def add_author(request):
    input_book_id = request.POST["input_book_id"]
    this_book = Book.objects.get(id=input_book_id)
    this_author = Author.objects.get(id=request.POST["selected"])
    this_book.authors.add(this_author)
    # return render(request, 'books_authors_app/added.html')
    return redirect(f'/view_book/{input_book_id}')

# -------------------------------------------------------

def authors(request):
    info={
        'authors': Author.objects.all(),
    }
    return render(request,'books_authors_app/authors.html', info)

def view_author(request, author_id):
    info={
        'author': Author.objects.get(id=author_id),
        'books': Book.objects.filter(authors__id=author_id),
        'book_drop': Book.objects.all(),
    }
    return render(request,'books_authors_app/view_author.html', info)

def create_author(request):
    Author.objects.create(first_name=request.POST['fn'], last_name=request.POST['ln'])
    return redirect('/authors')

def add_book(request):
    input_author_id = request.POST['input_author_id']
    this_author = Author.objects.get(id=input_author_id)
    this_book = Book.objects.get(id=request.POST['selected_book'])
    this_author.books.add(this_book)

    return redirect(f'/view_author/{input_author_id}')