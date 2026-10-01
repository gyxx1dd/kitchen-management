from django.contrib.auth.models import AbstractUser
from django.db import models

from kitchen_management import settings


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.username}"

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType,
                                  on_delete=models.CASCADE,
                                  related_name="dishes")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="dishes")

    def __str__(self) -> str:
        return f"{self.name}"