from django.urls import path
from .views import *

urlpatterns = [
    # Site
    path('', product_list, name='product_list'), # Aslida store_index edi, lekin sidebar product_list so'rayapti
    path('store/', product_list, name='store_index'), 
    path('filiallar/', filiallar_page, name='filiallar_page'),
    
    # Auth
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    # Admin Dashboard
    path('dashboard/', home_page, name='dashboard'),
    
    # Category CRUD
    path('category/list/', category_list, name='category_list'),
    path('category/create/', category_create, name='category_create'),
    path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),

    # Product CRUD
    path('product/list/', product_admin_list, name='product_admin_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),

    # Order Management
    path('order/list/', order_admin_list, name='order_admin_list'),
    path('orders/check-new/', check_new_orders, name='check_new_orders'),
    path('order/<int:pk>/detail/', order_detail, name='order_detail'),
    path('order/<int:pk>/status/<str:status>/', order_status_update, name='order_status_update'),
    path('order/<int:pk>/delete/', order_delete, name='order_delete'),
    path('orders/export/', export_orders_excel, name='export_orders_excel'),
    path('order/create/', order_create, name='order_create'),
    path('order/page/', order_page, name='order_page'),

    # Branch Management
    path('branch/list/', branch_list, name='branch_list'),
    path('branch/create/', branch_create, name='branch_create'),
    path('branch/<int:pk>/edit/', branch_edit, name='branch_edit'),
    path('branch/<int:pk>/delete/', branch_delete, name='branch_delete'),

    path('logs/', audit_log_list, name='audit_log_list'),

    # Cart
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/update/', update_cart, name='update_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('cart/modal/', cart_modal, name='cart_modal'),

]