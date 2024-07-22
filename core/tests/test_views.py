from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from core.models import Dish, DishType, Cook, Country

DISH_CREATE_URL = reverse("core:dish-create")
DISH_TYPE_CREATE_URL = reverse("core:dish-type-create")
COOK_CREATE_URL = reverse("core:cook-create")
COOK_LIST_URL = reverse("core:cook-list")


class PublicDishCreateTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(DISH_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishCreateTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_create(self):
        Dish.objects.create(name="pizza", price=100)
        Dish.objects.create(name="cheese", price=5)
        response = self.client.get(DISH_CREATE_URL)
        self.assertEqual(response.status_code, 200)


class PublicDishTypeCreateTest(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_TYPE_CREATE_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeCreateTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type_create(self):
        DishType.objects.create(name="soup")
        DishType.objects.create(name="pizza")
        response = self.client.get(DISH_TYPE_CREATE_URL)
        self.assertEqual(response.status_code, 200)


class PublicCookCreateTest(TestCase):
    def test_retrieve_cook_create(self):
        country = Country.objects.create(name="United States")
        Cook.objects.create_user(
            username="test7",
            password="test123",
            years_of_experience=12,
            country=country
        )
        response = self.client.get(COOK_CREATE_URL)
        self.assertEqual(response.status_code, 200)


class PublicCookListTest(TestCase):
    def test_retrieve_cook_list(self):
        country = Country.objects.create(name="United States")
        Cook.objects.create_user(
            username="test7",
            password="test123",
            years_of_experience=12,
            country=country
        )
        response = self.client.get(COOK_LIST_URL)
        self.assertEqual(response.status_code, 200)
