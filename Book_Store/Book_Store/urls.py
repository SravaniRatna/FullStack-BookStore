"""Book_Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import BookListCreate, BookRetrieveUpdateDestroy,book_list,book_update, book_delete
from django.views.decorators.csrf import csrf_exempt
from books.views import my_view
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = 'books'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('get-csrf-token/', csrf_exempt(my_view), name='get-csrf-token'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('',book_list,name='book_list'),
    path('book/<int:pk>/update/', book_update, name='book_update'),
    path('book/<int:pk>/delete/', book_delete, name='book_delete'),
]
