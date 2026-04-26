import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from adminapp.models import Category, Product

def import_data():
    print("Clearing old product data...")
    Product.objects.all().delete()
    
    print("Importing products...")
    
    # Categories
    cats = {
        'pitsa': Category.objects.get_or_create(name='Pitsa', slug='pitsa')[0],
        'burger': Category.objects.get_or_create(name='Burger', slug='burger')[0],
        'kombo': Category.objects.get_or_create(name='Kombo', slug='kombo')[0],
        'ichimliklar': Category.objects.get_or_create(name='Ichimliklar', slug='drinks')[0],
    }

    products_data = [
        # Pitsa
        ('Gavaya', 45000, 'pitsa', 'assets/img/pitza1.png'),
        ('Mexica', 53000, 'pitsa', 'assets/img/pitza2.png'),
        ('Hot achchiko', 64000, 'pitsa', 'assets/img/pitza3.png'),
        ('Mexica (Mini)', 45000, 'pitsa', 'assets/img/pitza4.png'),
        ('Apocalipo', 64000, 'pitsa', 'assets/img/pitza3.png'),
        ('Sosiskacho', 45000, 'pitsa', 'assets/img/pitza4.png'),
        
        # Burger
        ('Cheeseburger', 23000, 'burger', 'assets/img/burger.png'),
        ('Chili burger', 23000, 'burger', 'assets/img/burger.png'),
        ('Hamburger', 23000, 'burger', 'assets/img/burger.png'),
        ('Double Burger', 23000, 'burger', 'assets/img/burger.png'),
        
        # Kombo
        ('Kombo-1', 25000, 'kombo', 'assets/img/kombo1.png'),
        ('Kombo-2', 23000, 'kombo', 'assets/img/kombo2.png'),
        ('Kombo-3', 30000, 'kombo', 'assets/img/kombo1.png'),
        
        # Ichimliklar
        ('Sprite 1L', 6000, 'ichimliklar', 'assets/img/sprite.png'),
        ('Coca cola 1,5L', 9000, 'ichimliklar', 'assets/img/cola.png'),
        ('Fanta 1L', 6000, 'ichimliklar', 'assets/img/fanta.png'),
    ]

    for name, price, cat_key, img_path in products_data:
        Product.objects.create(
            name=name,
            category=cats[cat_key],
            price=price,
            image=img_path,
            description="Mazzali va sifatli mahsulot. MaxWay bilan hayotingiz mazzaliroq!"
        )

    print("Import complete!")

if __name__ == '__main__':
    import_data()
