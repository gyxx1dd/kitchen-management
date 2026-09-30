from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")