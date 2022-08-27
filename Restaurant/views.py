from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product,Category,RestaurantAccount,Table
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.http import HttpResponse
# Create your views here.
def home(request):
    p = Product.objects.all()
    c=Category.objects.all()
    r = RestaurantAccount.objects.all()
    t = Table.objects.all()
    data = {
        'p' : p,
        'c' : c,
        't':t,
        'r':r,

    }
    return render(request, 'home.html',data)

def Menu(request,id):
    category = Category.objects.filter(restaurant_id=id)
    data = {
        'category' : category
    }
    return render(request,'Restaurant/menu.html',data)

def restaurant_registration(request):
    if request.method == 'POST':
        restaurant_name = request.POST['restaurant_name']
        restaurant_Address = request.POST['restaurant_Address']
        restaurant_Contact = request.POST['restaurant_Contact']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        logo = request.POST['logo']

        if password == confirm_password:
            if RestaurantAccount.objects.filter(email=email).exists():
                messages.error(request, 'Username is taken')
                return redirect('signup')
            else:
                user = RestaurantAccount(restaurant_name=restaurant_name,restaurant_Address=restaurant_Address,restaurant_Contact=restaurant_Contact,email=email,password=password,logo=logo)
                user.save()

                return redirect('signin')
        else:
            messages.error(request, 'Password not match')
            return redirect('signup')
    return render(request, 'Form/restaurant_registrationform.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already exist')
                return redirect('signup')
            else:
                user = User.objects.create_user(password=password, email=email,username=email)
                user.save()
                return redirect('signin')
        else:
            messages.error(request, 'Password not match')
            return redirect('signup')
    return render(request,'Form/signupform.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']

        user = authenticate(request,username=email,password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('Menu',user.id)
        else:
            messages.error(request, 'invalid Credentials')
            return redirect('signin')
    return render(request,'Form/restaurant_loginform.html')

def alltable(request,id):
    table = Table.objects.filter(restaurant_id=id)
    data = {
        'table' : table,
    }
    return render(request,'Restaurant/alltable.html',data)

def createtable(request,id):
    if request.method=='POST':
        table_name = request.POST['table_name']
        status = request.POST.get('status')
        restaurant_id = request.POST.get('restaurant_id')
        if Table.objects.filter(table_name=table_name).filter(restaurant_id=restaurant_id):
            messages.error(request,'table name is exist')
            return redirect(reverse('createtable'))
        else:

            table=Table(table_name=table_name,status=status,restaurant_id=restaurant_id)
            table.save()
            return redirect('/')
    else:
        return render(request,'Form/tableform.html')

def allcategories(request,id):
    category = Category.objects.filter(restaurant_id=id)
    data = {
        'category':category,
    }

    return render(request,'Restaurant/allcategories.html',data)

def createcategory(request,id):
    if request.method=='POST':
        restaurant_id = request.POST.get('restaurant_id')
        category_name = request.POST['category_name']
        status = request.POST.get('status')

        if Category.objects.filter(category_name=category_name).exists():
            messages.error(request, 'category is already in the list')
            return redirect(reverse('createcategory'))
        else:
            cat = Category(restaurant_id=restaurant_id,category_name=category_name,status=status)
            cat.save()
            return redirect(createproduct)

    return render(request,'Form/Categoryform.html')

def allproduct(request,id):
    product = Product.objects.filter(restaurant_id=id)
    print(id)
    data = {
        'product':product,
    }
    return render(request,'Restaurant/allproduct.html',data)

def createproduct(request,id):
    categories = Category.objects.filter(restaurant_id=id)
    if request.method == 'POST':
        restaurant_id = request.POST.get('restaurant_id')
        product_name = request.POST['product_name']
        product_price= request.POST['product_price']
        description = request.POST['description']
        image = request.FILES.get('image')
        category_name = request.POST.get('category_name')
        status = request.POST.get('status')
        print(category_name)
        product = Product(restaurant_id=restaurant_id,category_name=category_name,status=status,product_name=product_name,product_price=product_price,image=image)
        product.save()
        return redirect('/')

        pass
    else:
        data = {
            'categories':categories,
        }
    return render(request,'Form/productform.html',data)