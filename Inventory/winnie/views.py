from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signin, ProductDetails

def home_view(request):
    return render(request, 'home.html')

def starttrial(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        e = Signin()
        e.name = username
        e.email = email
        e.passw = password
        e.save()

        messages.success(request, 'Account created successfully!')
        return redirect('winnie:home')  # Redirect to the home page

    return render(request, 'StartTrial.html')

def products(request):
    if request.method == "POST":
        proname = request.POST.get("productName")
        category = request.POST.get("category")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        description = request.POST.get("description")

        e = ProductDetails()
        e.proname = proname
        e.category = category
        e.quantity = quantity
        e.price = price
        e.description = description
        e.save()

        messages.success(request, 'Product has been added successfully!')
        return redirect('winnie:home')  # Redirect to the home page

    return render(request, 'Products.html')
