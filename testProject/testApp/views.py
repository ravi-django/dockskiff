from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ProductForm, signupform
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required()
def retrieve_view(request):
    products = Product.objects.all()
    messages.success(request, 'now you can add')

    return render(request, 'testApp/index.html', {'products': products})


@login_required()
def create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'testApp/create.html', {'form': form})


@login_required()
def delete_view(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')


@login_required()
def update_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'testApp/update.html', {'product': product})


@login_required()
def logoutview(request):
    logout(request)
    return redirect('/')


def signup(request):
    form = signupform()
    if request.method == 'POST':
        form = signupform(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('retrieve_view')
    return render(request, 'testApp/signup.html', {'form': form})
