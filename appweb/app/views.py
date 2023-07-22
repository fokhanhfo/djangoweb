from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login,decorators,logout
from django.contrib import messages

# Create your views here.

def home(request):
    products =Product.objects.all()
    category = Category.objects.all()

    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order=[]
    context ={'items': items,'order': order,'products': products,'category': category}
    return render(request,'app/home.html',context)

def category(request,Category_id):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer,complate=False)
    else:
        order=[]
    products =Product.objects.all()
    category = Category.objects.all()
    categoryid= Category.objects.get(pk=Category_id)
    context ={'category': category,'categoryid': categoryid,'products':products,'order': order}
    return render(request,'app/category.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
    else:
        order=[]
        items=[]
    context ={'items': items,'order': order}
    return render(request,'app/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_items':0,'get_cart_total':0}
    context ={'items': items,'order': order}
    return render(request,'app/checkout.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        q=CreateUserForm(request.POST)
        if q.is_valid():
            q.save()
    context = {'form': form}
    return render(request,'app/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        user_name = request.POST.get('taikhoan')
        matkhau = request.POST.get('matkhau')
        my_user = authenticate(request,username=user_name, password=matkhau)
        if my_user is not None :
            login(request,my_user)
            return redirect('home')
        else:messages.info(request,'Mật khẩu hoặc tài khoản sai ')
    context={}
    return render(request,'app/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def updateItem(request):
    # json để biến chuỗi thành đối tượng và request.body là để gửi dữ liệu http
    data =json.loads(request.body)
    productID=data['productID']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=productID)
    order,created = Order.objects.get_or_create(customer=customer,complate=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        orderItem.quantity+=1
    elif action == 'remove':
        orderItem.quantity-=1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('added', safe=False)

def search(request):
    if request.method == 'POST':
        searchs=request.POST.get('searched')
        keys=Product.objects.filter(name__contains=searchs)
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer,complate=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order=[]
    context={"searchs":searchs, "keys":keys,'items': items,'order': order}
    return render(request, 'app/search.html', context)

def view(request,Product_id):
    productsid=Product.objects.get(pk=Product_id)
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create(customer=customer,complate=False)
    else:
        order=[]
    context ={'order': order,'productsid': productsid}
    return render(request, 'app/view.html', context)