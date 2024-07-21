from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from core.models import Dish

DISH_CREATE_URL = reverse("core:dish-create")


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

