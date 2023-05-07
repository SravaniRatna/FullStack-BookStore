from rest_framework import generics
from .models import Book
from .forms import BookForm
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render, redirect,get_object_or_404


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

def my_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_list.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:book_detail', pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
