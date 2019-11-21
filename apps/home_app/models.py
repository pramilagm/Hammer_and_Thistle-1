from django.db import models
from datetime import date
from apps.login_app.models import *

class Artist(models.Model):
    name = models.CharField(max_length=255)
    images = models.ImageField()
    des = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ring(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    metal = models.CharField(max_length=255)
    stone = models.CharField(max_length=255)
    size = models.IntegerField()
    finish = models.CharField(max_length =255)
    recommended_pair = models.ImageField()
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    artist = models.ForeignKey(Artist,related_name ="rings")
    ring_image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Necklace(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    metal = models.CharField(max_length=255)
    stone = models.CharField(max_length=255)
    recommended_pair = models.ImageField()
    chain_image = models.ImageField()
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    artist = models.ForeignKey(Artist,related_name ="necklaces")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bespoke(models.Model):
    images = models.ImageField()
    metals = models.CharField(max_length=255)
    form_factor = models.TextField()
    stone = models.CharField(max_length=255)
    stone_size = models.CharField(max_length=255)
    theme = models.TextField()
    finish = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name = "bespokes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    street : models.CharField(max_length=255)
    city : models.CharField(max_length=255)
    state_initials : models.CharField(max_length=2)

class Event(models.Model):
    location = models.ForeignKey(Address , related_name ="locations")
    description = models.TextField()
    artist = models.ForeignKey(Artist,related_name ="events")

class Recommended(models.Model):
    rings = models.ForeignKey(Ring,related_name ="rings_recommendation")
    necklaces = models.ForeignKey(Necklace , related_name ="necklace_recommendation")

class Product(models.Model):
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)