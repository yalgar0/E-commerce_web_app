
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrakingStatus'),
    path('search/',views.search,name='Search'),
    path('productview/',views.productView,name='Search'),
    path('checkout/',views.index,name='Checkout')
]