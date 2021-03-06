"""CSHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tabnanny import check
from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware
from .views.roomchat import checkview, room, send, getMessages
from .views.search import search
from .views.product_detail import ProductDetailViews
# CHIEN: Tạo đường dẫn URL để xử lý yêu cầu
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup' , Signup.as_view()),
    path('store', store, name='store'),


    #HOANG: thêm đường dẫn login
    # CHIEN: as_view()phương thức lớp trả về một hàm có thể được gọi khi một yêu cầu đến cho một URL khớp với mẫu được liên kết.
    path('login', Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart', Cart.as_view(),name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('product_detail',ProductDetailViews.as_view(), name='product_detail'),
    path('checkview', checkview, name='checkview'),
    path('<str:room>/', room, name='room'),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
    path('search',search,name='search'),
    
    
]
