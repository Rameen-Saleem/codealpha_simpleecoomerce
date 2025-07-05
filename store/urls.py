from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update-cart/<int:pk>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
]
