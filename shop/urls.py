
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import index, detail, checkout, CreateProduct, DeleteProduct
from rest_framework import routers 

router = routers.SimpleRouter()
router.register('create', CreateProduct)

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
    path('checkout/', checkout, name='checkout'),
    path('delete/<int:pk>/', DeleteProduct),

]

urlpatterns += router.urls