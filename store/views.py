from django.shortcuts import render
from .models import *

from django.http import JsonResponse
# Create your views here.

def store(request):
     products = Product.objects.all()
     context = {'products':products}
     return render(request, 'store/store.html', context)

def cart(request):
     ## once call cart url/API
     ## conditions, if user logged in
     if request.user.is_authenticated:
          customer = request.user.customer
          ## get_or_created(defaults=None, **kwargs):
          ## return: tuple of (object, created)
          ##   object: the retrieved or creatd object
          ##   created: boolean whether new object was created
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all() ## get all the order items from the parent order. (childObjects_set)
     else: ## if not loggin user, items will be empty for now
          ## TODO: build replica mechinism when user logged in
          items = []
          order = {'get_cart_total':0, 'get_cart_items':0}
     context = {'items':items, 'order':order}
     return render(request, 'store/cart.html', context)

def checkout(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
     else: ## if not loggin user, items will be empty for now
               ## TODO: build replica mechinism when user logged in
               items = []
               order = {'get_cart_total':0, 'get_cart_items':0}
     context = {'items':items, 'order':order}
     return render(request, 'store/checkout.html', context)

def updateItem(request):
     return JsonResponse('Item was added', safe=False)