from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType


class PublicDishTest(TestCase):
    def test_login_required(self):
        url = reverse("kitchen:dish-list")
        res = self.client.get(url)

        self.assertNotEqual(res.status_code, 200)

    def test_context_data(self):
        self.obj_user = get_user_model().objects.create_superuser(
            username="vasia",
            password="1234312loS_",
        )
        self.client.force_login(self.obj_user)

        data = {
            "name": "sushi",
        }
        url = reverse("kitchen:dish-list")
        res = self.client.get(url, data)

        self.assertEqual(res.context["form"].initial["name"], "sushi")

    def test_queryset(self):
        self.obj_user = get_user_model().objects.create_superuser(
            username="vasia",
            password="1234312loS_",
        )
        self.client.force_login(self.obj_user)
        dish_type = DishType.objects.create(name="fish")
        Dish.objects.create(
            name="sushi",
            description="lafa",
            price=12,
            dish_type=dish_type
        )
        dishes = Dish.objects.all()
        data = {
            "name": "sushi",
        }
        url = reverse("kitchen:dish-list")
        res = self.client.get(url, data)

        self.assertEqual(list(res.context["dish_list"]),
                         list(dishes))


class PrivateRegisterTest(TestCase):
    def test_login_required(self):
        url = reverse("kitchen:register")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_template_name(self):
        url = reverse("kitchen:register")
        res = self.client.get(url)

        self.assertTemplateUsed(res, "registration/register.html")

