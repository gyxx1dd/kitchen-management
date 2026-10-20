from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.obj_user = get_user_model().objects.create_superuser(
            username="vasia",
            password="1234312loS_",
        )

        self.obj_cook = get_user_model().objects.create_user(
            username="vasia2",
            password="wefwefk3S_",
            years_of_experience=2,
        )

        self.client.force_login(self.obj_user)

    def test_cook_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.obj_cook.years_of_experience)

    def test_cook_detail_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_change", args=[self.obj_cook.id])
        res = self.client.get(url)

        self.assertContains(res, self.obj_cook.years_of_experience)