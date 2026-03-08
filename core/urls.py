from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.db import transaction

# 命名空间
app_name = 'core'

urlpatterns = [
    # ==============================
    # 1. 商品浏览 (Block A & B)
    # ==============================
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # ==============================
    # 2. 用户认证 (Block A1-A2)
    # ==============================
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:product_list'), name='logout'),
    path('register/', views.register, name='register'),

    # ==============================
    # 3. 购物车 (Block A7-A10)
    # ==============================
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # ==============================
    # 4. 订单系统 (Block A11-A13) 
    # ==============================
    # 结算动作 (对应 cart_detail.html 里的按钮)
    path('checkout/', views.checkout, name='checkout'),
    # 订单历史
    path('orders/', views.order_list, name='order_list'),
    # 订单详情
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('cart/update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
     path('orders/<int:pk>/cancel/', views.cancel_order, name='cancel_order'),
    # ==============================
    # 5. 商家后台 (Vendor Portal)
    # ==============================
    path('vendor/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor/products/', views.vendor_product_list, name='vendor_product_list'),
    path('vendor/products/add/', views.vendor_product_add, name='vendor_product_add'),
    path('vendor/products/<int:pk>/edit/', views.vendor_product_edit, name='vendor_product_edit'),
    
    path('vendor/orders/', views.vendor_order_list, name='vendor_order_list'),
    path('vendor/orders/<int:pk>/', views.vendor_order_detail, name='vendor_order_detail'),
    path('vendor/products/<int:pk>/delete/', views.vendor_product_delete, name='vendor_product_delete'),

    # ==============================
    # 5. 数据报告与分析 (Block V)
    # ==============================
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
]
