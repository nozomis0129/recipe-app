from django.test import TestCase
from .models import User

# Create your tests here.


class UserModelTest(TestCase):
    def setUpTestData():
        User.objects.create(username="Tom", password="tomspsw")

    def test_user_name(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("username").verbose_name
        self.assertEqual(field_label, "username")

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("username").max_length
        self.assertEqual(max_length, 150)

    def test_user_name(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("password").verbose_name
        self.assertEqual(field_label, "password")

    def psw_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("password").max_length
        self.assertEqual(max_length, 100)
