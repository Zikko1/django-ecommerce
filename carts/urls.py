from django.urls import path
from . import views

urlpatterns = [
    path('',views.Cart, name="cart"),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart')
]
