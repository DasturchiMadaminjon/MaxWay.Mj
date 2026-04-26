from django import forms
from .models import Category, Product, Order, OrderItem, Branch

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "slug": forms.TextInput(attrs={'class':'form-control'}),
        }

class ProductForm(forms.ModelForm):
    price = forms.DecimalField(min_value=1, widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "category": forms.Select(attrs={'class':'form-control'}),
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "description": forms.Textarea(attrs={'class':'form-control', 'rows': 3}),
            "image": forms.FileInput(attrs={'class':'form-control'}),
            "available": forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class':'form-control'}),
            "phone": forms.TextInput(attrs={'class':'form-control phone-mask', 'placeholder':'+998 (__) ___-__-__'}),
            "address": forms.Textarea(attrs={'class':'form-control', 'rows': 2}),
            "payment_method": forms.Select(attrs={'class':'form-control'}),
            "status": forms.Select(attrs={'class':'form-control'}),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"
        widgets = {
            "order": forms.Select(attrs={'class':'form-control'}),
            "product": forms.Select(attrs={'class':'form-control'}),
            "price": forms.NumberInput(attrs={'class':'form-control'}),
            "quantity": forms.NumberInput(attrs={'class':'form-control'}),
        }

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Filial nomi'}),
            "address": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manzil'}),
            "phone": forms.TextInput(attrs={'class':'form-control phone-mask', 'placeholder':'+998 (__) ___-__-__'}),
            "working_hours": forms.TextInput(attrs={'class':'form-control', 'placeholder':'09:00 - 23:00'}),
            "location_url": forms.TextInput(attrs={'class':'form-control', 'placeholder':'Google Maps Link'}),
            "latitude": forms.NumberInput(attrs={'class':'form-control', 'placeholder':'41.3110'}),
            "longitude": forms.NumberInput(attrs={'class':'form-control', 'placeholder':'69.2410'}),
        }