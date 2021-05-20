from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Order, Product
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, response
from rest_framework import serializers
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.

def index(request):

    prod_objects = Product.objects.all()

    # Search Code
    item_name = request.GET.get('item_name')
    if item_name != ' ' and item_name is not None:
        prod_objects = prod_objects.filter(title__icontains=item_name)

    # Paginator Code
    paginator = Paginator(prod_objects, 4)
    page = request.GET.get('page')
    prod_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'prod_objects':prod_objects})


def detail(request, id):

    prod_objects = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'prod_objects': prod_objects})


def checkout(request):

    if request.method == "POST":

        items = request.POST.get('items', "")
        name = request.POST.get('name',"")
        email = request.POST.get("email","")
        address = request.POST.get("address","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        zip = request.POST.get("zip","")
        total = request.POST.get("total", "")
    
        order = Order(items = items, name=name, email=email, address=address, city=city, state=state, zip=zip, total=total)
        order.save()


    return render(request, 'shop/checkout.html')



class CreateProduct(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProduct(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



@api_view(['DELETE'])
def DeleteProduct(request, pk):

    product = Product.objects.get(id=pk)
    product.delete()

    return Response("Item deleted")
    


    




