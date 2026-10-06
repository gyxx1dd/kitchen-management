from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish, Table, Reservation


class ModelsTest(TestCase):
    def test_dish_type_str(self):
        obj_dish_type = DishType.objects.create(name="Spaghetti")
        self.assertEqual(str(obj_dish_type), obj_dish_type.name)

    def test_cook_str(self):
        obj_cook = get_user_model().objects.create_user(
            username="vasia",
            password="123123S_",
            years_of_experience=2,
        )
        self.assertEqual(str(obj_cook), obj_cook.username)

    def test_dish_str(self):
        obj_dish_type = DishType.objects.create(name="Spaghetti")
        obj_cook = get_user_model().objects.create_user(
            username="vasia",
            password="123123S_",
            years_of_experience=2,
        )
        obj_dish = Dish.objects.create(
            name="fish",
            description="tasty",
            price=12,
            dish_type=obj_dish_type,
        )
        obj_dish.cooks.add(obj_cook)
        self.assertEqual(str(obj_dish), obj_dish.name)
        self.assertEqual(obj_dish.name, "fish")
        self.assertEqual(obj_dish.price, 12)

    def test_table_str(self):
        obj_table = Table.objects.create(
            number=12
        )
        self.assertEqual(str(obj_table), "12")

    def test_reservation_create(self):
        obj_user = get_user_model().objects.create_user(
            years_of_experience=12,
            username="vasia",
            password="2131424S_"
        )

        table = Table.objects.create(number=1)

        obj_reservation = Reservation.objects.create(
            user=obj_user,
            table=table,
            date="2026-10-01",
            time_start="18:30",
            time_end="19:30",
        )

        self.assertEqual(obj_reservation.user.username, obj_user.username)
        self.assertEqual(obj_reservation.table.number, table.number)
        self.assertEqual(obj_reservation.date, "2026-10-01")
        self.assertEqual(obj_reservation.time_start, "18:30")
        self.assertEqual(obj_reservation.time_end, "19:30")
