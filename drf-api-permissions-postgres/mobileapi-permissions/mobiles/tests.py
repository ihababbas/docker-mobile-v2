from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Mobile

from django.urls import reverse

class ThingTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_thing = Mobile.objects.create(
            main_type="Xiaomi Redmi",
            owner=testuser1,
            description="Best mobile.",
            model_type = "Note 11",
            battary_size = 5000,
            price = 175,
            colors = "black , blue"
            
        )
        test_thing.save()


    def setUp(self):
        self.client.login(username='testuser1', password="pass")




    def test_things_model(self):
        thing = Mobile.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_name = str(thing.main_type)
        actual_description = str(thing.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Xiaomi Redmi")
        self.assertEqual(
            actual_description, "Best mobile."
        )

    def test_get_thing_list(self):
        url = reverse("thing_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        

    def test_auth_required(self):
        self.client.logout()
        url = reverse("thing_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("thing_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)