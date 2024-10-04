

from django.urls import path
from .views import book_table, success

urlpatterns = [
    path('book/', book_table, name='book_table'),
    path('success/', success, name='success'),
]