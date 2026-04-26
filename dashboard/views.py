from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from . import services
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# AUTH
def login_page(request):
    if request.POST:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user: 
            login(request, user)
            return redirect("home_page")
    return render(request, 'login.html')

@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return redirect("login_page")

# DASHBOARD
@login_required(login_url='login_page')
def home_page(request):
    ctx = { 'counts': {
        'categories': Category.objects.count(),
        'products': Product.objects.count(),
        'orders': Order.objects.count(),
        'branches': Branch.objects.count(),
    }}
    return render(request, 'index.html', ctx)

# CATEGORY CRUD
@login_required(login_url='login_page')
def category_list(request):
    return render(request, 'category/list.html', {'categories': services.get_categories()})

@login_required(login_url='login_page')
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category/form.html', {'form': form})

@login_required
def category_edit(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category/form.html', {'form': form, 'obj': obj})

@login_required
def category_delete(request, pk):
    get_object_or_404(Category, pk=pk).delete()
    return redirect('category_list')

# PRODUCT CRUD
@login_required(login_url='login_page')
def product_list(request):
    return render(request, 'product/list.html', {'products': services.get_products()})

@login_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product/form.html', {'form': form})

@login_required
def product_edit(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product/form.html', {'form': form, 'obj': obj})

@login_required
def product_delete(request, pk):
    get_object_or_404(Product, pk=pk).delete()
    return redirect('product_list')

# ORDER LIST
@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order/list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order/detail.html', {'order': order})

@login_required
def profile(request):
    ctx = { 'counts': {
        'categories': Category.objects.count(),
        'products': Product.objects.count(),
        'orders': Order.objects.count(),
        'branches': Branch.objects.count(),
    }}
    return render(request, 'profile.html', ctx)
