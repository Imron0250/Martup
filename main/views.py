from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def home(request, ):
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info': Info.objects.last(),
        'width': Import_width.objects.all()[:3],
        'category': Category.objects.all()[:3],
        'best': Best.objects.all()[:3],
        'products': Products.objects.all()[:4],
        'product':  Product.objects.all(),
        'slider': Slider.objects.all()[:5],
        'email_titles': Email_titles.objects.last(),
        'app': App.objects.last(),
    }
    return render(request, 'index-2.html', context)

def post_mail(request):
    if request.method == "POST":
        email = request.POST.get("email")
        Email.objects.create(email=email)
    return redirect("home")

def product_details(request,pk):
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info': Info.objects.last(),
        'width': Import_width.objects.last(),
        'clothes': Clothes.objects.last(),
        'clothe': Clothe.objects.last(),
        'product':  Product.objects.get(id=pk),
        'products':  Product.objects.all(),

    }
    return render(request, "product-details-default.html", context )

def product_details_left(request):
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info': Info.objects.last(),
        'width': Import_width.objects.last(),
        'products':  Product.objects.last(),
        'productes':  Product.objects.all(),
    }
    return render(request, 'product-details-left-sidebar.html', context)

def contact(request):
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info': Info.objects.last(),
        'width': Import_width.objects.last(),
        'map': Map.objects.last()
    }
    return render(request, 'contact.html', context)



def shop_full(request):
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info': Info.objects.last(),
        'product':  Product.objects.all(),
        'shop_width': Shop_width.objects.last()
    }
    return render(request, 'shop-sidebar-full-width.html', context)

def cart(request):
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info': Info.objects.last(),
        'width': Import_width.objects.last(),
        'product':  Product.objects.all(),

    }
    return render(request, 'cart.html', context)

def add_card(request, pk):
    user = request.user
    if Card.objects.filter(user=user, product_id=pk).count()> 0:
        pass
    else:
        Card.objects.create(user=user, product_id=pk)

    return redirect('home')

def delete_card(request, pk):
    Card.objects.get(id=pk).delete()
    return redirect('home')

def card_view(request):
    user = request.user
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info' : Info.objects.last(),
    }
    return render(request, 'cart.html', context)


def create_order(request):
    if request.method == "POST":
        name  = request.POST.get("name")
        email = request.POST.get("email")
        notes = request.POST.get("notes")
        message = request.POST.get('message')
        user = request.user
        Order.objects.create(
            name = name,
            email = email,
            notes = notes,
            user = user,
            message = message,
            total =0
        )
        return redirect("contact")
    return redirect("contact")

def about(request):
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info' : Info.objects.last(),
        'best_forever': Best_forever.objects.last(),
        'slider': Slider.objects.all()[:5],
        'email_titles': Email_titles.objects.last(),
        'app': App.objects.last(),
        'best': Best.objects.all()[:3],

    }
    return render(request, 'about.html',context)

def faq(request):
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'width': Import_width.objects.last(),
        'info' : Info.objects.last(),
        'faq': Faq.objects.all()
        
    }
    return render(request, 'faq.html', context)

def login_vews(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('home')
            else:
                return redirect('login')
        else:
            return redirect('login')

    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info' : Info.objects.last(),
        'width': Import_width.objects.last(),
        
    }
    return render(request, 'login.html',context)

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(password, username)
        User.objects.create_user(password=password, username=username)
    return redirect("login")

def logout_vews(request):
    logout(request)
    return redirect("home")

def shop(request):
    
    user = request.user
    card = []
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info' : Info.objects.last(),
        'product': Product.objects.all().order_by('-id'),
        'product' : Product.objects.all(),

    }
    return render(request, 'shop-sidebar.html',context)

def logout_vews(request):
    logout(request)
    return redirect("home")

def blog(request):
    context = {
        'Blog_widht': Blog_widhh.objects.last(),
        'Photo_blog': Photo_blog.objects.last(),
        'Post_blog': Post_blog.objects.all(),
        'People_model': People_model.objects.last(),
        'info' : Info.objects.last(),
        'email_titles': Email_titles.objects.last(),
        'app': App.objects.last(),
        
    }
    return render(request, 'blog-details-full-width.html', context)

def checkout(request):
    user = request.user
    items = 0
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        items = card.count()
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        'items' : items,
        'card': card,
        'total': total,
        'info' : Info.objects.last(),
        'width': Import_width.objects.last(),
        'card' : Card.objects.all(),


    }
    return render(request, 'checkout.html', context)

def create_order(request):
    if request.method == "POST":
        fname  = request.POST.get("fname")
        lname  = request.POST.get("lname")
        region  = request.POST.get("region")
        adress1  = request.POST.get("adress1")
        adress2 = request.POST.get("adress2")
        phone  = request.POST.get("phone")
        email = request.POST.get("email")
        notes = request.POST.get("notes")
        user = request.user
        order = Order2.objects.create(
            fname = fname,
            lname = lname,
            region = region,
            adress1 = adress1,
            adress2 = adress2,
            phone = phone,
            email = email,
            notes = notes,
            user = user,
            total =0
        )
        for i in Card.objects.filter(user=user):
            OrderItem.objects.create(order=order, product=i.product, price = i.product.bonus if i.product.price > 0 else i.product.price)
            order.total += i.product.bonus if i.product.bonus > 0 else i.product.price
        order.save()
        Card.objects.filter(user=user).delete()
        return redirect("checkout")
    return redirect("checkout")