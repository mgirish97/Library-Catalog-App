from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Book

def index(request):
    book_list = Book.objects.order_by('-author_lastname')
    context = {"book_list": book_list}
    return render(request, "library/index.html", context)

def item(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Item does not exit")
    return render(request, 'library/item.html', {'book': book})

def login(request):
    return render(request, "library/login.html")

