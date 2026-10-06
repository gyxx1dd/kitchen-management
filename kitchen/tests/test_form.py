from django.db.models import Model
from django.test import TestCase

from kitchen.forms import CookCreationForm, CookUpdateForm
from kitchen.models import Dish, DishType


class FormsTests(TestCase):
    def test_creation_form_with_years_of_experience(self):
        data = {
            "username": "vasia",
            "password1": "123123L_",
            "password2": "123123L_",
            "years_of_experience": 12,
        }
        form = CookCreationForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)

    def test_cook_update_form(self):
        dish_type = DishType.objects.create(
            name="seafood"
        )

        Dish.objects.create(
            name="fish",
            description="super",
            price=12,
            dish_type=dish_type
        )

        data = {
            "username": "example",
            "years_of_experience": 12,
            "first_name": "test1",
            "last_name": "test2",
            "dish": Dish.objects.all(),
        }

        form = CookUpdateForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(list(form.cleaned_data), list(data))