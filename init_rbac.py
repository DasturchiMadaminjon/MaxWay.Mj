import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from adminapp.models import Order, Product, Category, Branch

def setup_rbac():
    # 1. Create Groups
    manager_group, created = Group.objects.get_or_create(name='Manager')
    cashier_group, created = Group.objects.get_or_create(name='Cashier')
    
    # 2. Assign Permissions to Manager
    # Manager can manage Products, Categories, and view Orders
    p_content_type = ContentType.objects.get_for_model(Product)
    c_content_type = ContentType.objects.get_for_model(Category)
    o_content_type = ContentType.objects.get_for_model(Order)
    b_content_type = ContentType.objects.get_for_model(Branch)
    
    # Simple way: assign all permissions for these models to manager
    mgr_permissions = Permission.objects.filter(content_type__in=[p_content_type, c_content_type, b_content_type, o_content_type])
    manager_group.permissions.set(mgr_permissions)
    
    # 3. Assign Permissions to Cashier
    # Cashier can only see and edit Orders
    cash_permissions = Permission.objects.filter(content_type=o_content_type)
    cashier_group.permissions.set(cash_permissions)
    
    print("RBAC Groups and Permissions successfully initialized!")

if __name__ == "__main__":
    setup_rbac()
