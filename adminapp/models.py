from django.db import models

class AuditLog(models.Model):
    user = models.ForeignKey(
        "auth.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="audit_logs",
    )
    action = models.CharField(max_length=32)  # create/edit/delete/login/logout
    entity = models.CharField(max_length=64)  # Category/Product/Order/...
    entity_id = models.PositiveBigIntegerField(null=True, blank=True)
    message = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Audit log"
        verbose_name_plural = "Audit loglar"

    def __str__(self):
        return f"{self.created_at:%Y-%m-%d %H:%M} {self.user} {self.action} {self.entity}({self.entity_id})"


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products/', blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    payment_method = models.CharField(max_length=50, default='cash')
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='New')

    def __str__(self):
        return f"Order {self.id} by {self.first_name}"

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    class Meta:
        verbose_name = "Buyurtma elementi"
        verbose_name_plural = "Buyurtma elementlari"


class Branch(models.Model):
    name = models.CharField(max_length=200, verbose_name="Filial nomi")
    address = models.CharField(max_length=300, verbose_name="Manzil")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
    working_hours = models.CharField(max_length=100, verbose_name="Ish vaqti")
    location_url = models.CharField(max_length=500, blank=True, verbose_name="Google Maps linki")
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True, verbose_name="Kenglik (Latitude)")
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True, verbose_name="Uzunlik (Longitude)")
    
    def __str__(self):
        return self.name

    @property
    def get_map_url(self):
        if self.latitude and self.longitude:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}&hl=uz&z=15"
        if not self.location_url:
            return "#"
        if self.location_url.startswith('http'):
            return self.location_url
        if ',' in self.location_url:
            # Assume coordinates in URL field as backup
            return f"https://www.google.com/maps/search/?api=1&query={self.location_url}"
        return f"https://www.google.com/maps/search/?api=1&query={self.location_url}"

    class Meta:
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"
