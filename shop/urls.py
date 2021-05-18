
from django.contrib import admin
from django.urls import path, include
from .views import index, detail, checkout

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
    path('checkout/', checkout, name='checkout')
]
