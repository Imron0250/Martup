from django.db import models
from django.contrib.auth.models import User


class Info(models.Model):
    logo = models.ImageField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.CharField(max_length=2555)
    instagram = models.CharField(max_length=2555)
    pinterest = models.CharField(max_length=2555)
    driblee = models.CharField(max_length=2555)
    products_photo = models.ImageField()
    banner = models.ImageField()
    company_logo = models.ImageField()
    company_name = models.CharField(max_length=255)
    about_width = models.ImageField()

class Import_width(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField()


class Category(models.Model):
    img = models.ImageField()

class Best(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()

class Products(models.Model):
    img = models.ImageField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    bonus = models.IntegerField(default=0)
    photo = models.ImageField(blank=True)
    despictions = models.TextField()

class Slider(models.Model):
    img = models.ImageField()

class Email(models.Model):
    email = models.EmailField()

class Email_titles(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

class App(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    app_store = models.TextField()
    google_play = models.TextField()

class Clothes(models.Model):
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()

class Clothe(models.Model):
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Shop_width(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    shop_title = models.CharField(max_length=255)
    img = models.ImageField()

class Map(models.Model):
    location = models.CharField(max_length=2555)

class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    total = models.IntegerField()
    message = models.TextField()

class Best_forever(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField()
    video = models.CharField(max_length=266666)

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

class Blog_widhh(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    img = models.ImageField()
    text = models.TextField()
    img2 = models.ImageField()

class Photo_blog(models.Model):
    text = models.TextField()
    img = models.ImageField()

class People_model(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)

class Post_blog(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    date =  models.DateField()
    text = models.TextField()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.IntegerField()

class Order2(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    adress1 = models.CharField(max_length=255)
    adress2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    total = models.IntegerField()

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.IntegerField()
