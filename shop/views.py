from django.shortcuts import render
from .models import Order, Product
from django.core.paginator import Paginator

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