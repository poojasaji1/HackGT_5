
from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    eco_friendly = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    carbon_footprint = models.BooleanField(default=False)
    locally_made = models.BooleanField(default=False)
    recyclable = models.BooleanField(default=False)
    sustainable_packaging = models.BooleanField(default=False)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.user = None

    def __str__(self):
        return f"{self.name} by {self.seller.user.username}"

# Create your models here.
