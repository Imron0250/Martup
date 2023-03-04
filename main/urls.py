from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('post-mail/', post_mail, name='post-mail'),
    path('product_details_left/', product_details_left, name='product_details_left'),
    path('product-details/<int:pk>/', product_details, name='product_details'),
    path('cart/', cart, name='cart'),
    path('shop_full/', shop_full, name='shop_full'),
    path('add-card/<int:pk>/', add_card, name='add-card'),
    path('delete-card/<int:pk>/', delete_card, name='delete-card'),
    path('contact/', contact, name='contact'),
    path('create-order/', create_order, name='create-order'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('login/', login_vews, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_vews, name='logout'),
    path('blog/',blog, name='blog'),
    path('checkout/', checkout, name='checkout'),
    path('create-order/', create_order, name='create-order'),
    
]