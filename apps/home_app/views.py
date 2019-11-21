from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from apps.home_app.models import *
from apps.login_app.models import *
import bcrypt

def index(request):
    if 'total_quantity' not in request.session:
        request.session['total_quantity'] = 0
        request.session['total_charge']  = 0

    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def home(request):
    return render (request, 'home_app/index.html')

def cart(request):
    return render (request, 'home_app/cart.html')

def cart_add(request):
    # logic for adding to cart here
    return redirect ('/cart')

def checkout(request):
    if request.method =="POST":
        quantity_from_form =int(request.POST["quantity"])
        id_from_form = int(request.POST["product_id"])
        price = Product.objects.get(id=id_from_form).price
        total_charge = quantity_from_form *float(price)
        if 'total_quantity' in request.session:
            request.session['total_quantity'] += quantity_from_form
            request.session['total_charge']  += total_charge
            request.session['recent_charge'] = total_charge
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect('/checkout')

    if request.method=="GET":
        context = {
            'total_price' : request.session['total_charge']  ,
            'total_quantity' : request.session['total_quantity'],
            'price': request.session['recent_charge']
        }
        return render(request, "store/checkout.html",context)

def product(request): 
    return render (request, 'home_app/product.html') #, context
    # ,item_id - needs to be added
    # context = {
    #     # 'target_ring' : Ring.objects.get(id = item_id)
    #     # 'target_necklace' : Necklace.objects.all(id = item_id)
    #     'impulse_buy' : Recommended.objects.all()
    # }

def products(request):
    return render (request, 'home_app/products.html' ) #, context
    # context = {
    #     'all_rings' : Ring.objects.all(),
    #     'all_necklaces' : Necklace.objects.all(),
    #     'impulse_buy' : Recommended.objects.all()
    # }

def text_page(request):
    return render (request, 'home_app/text-page.html')

def logout(request): 
    if 'logged_in' in request.session:
        request.session.clear()
    return redirect('/')
