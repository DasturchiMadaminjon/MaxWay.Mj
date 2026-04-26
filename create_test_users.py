import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User, Group

def create_test_users():
    # Manager User
    manager_user, created = User.objects.get_or_create(username='manager_test')
    if created:
        manager_user.set_password('pass1234')
        manager_user.save()
    
    manager_group = Group.objects.get(name='Manager')
    manager_user.groups.add(manager_group)
    
    # Cashier User
    cashier_user, created = User.objects.get_or_create(username='cashier_test')
    if created:
        cashier_user.set_password('pass1234')
        cashier_user.save()
    
    cashier_group = Group.objects.get(name='Cashier')
    cashier_user.groups.add(cashier_group)
    
    print("Test users created: manager_test / pass1234, cashier_test / pass1234")

if __name__ == "__main__":
    create_test_users()
