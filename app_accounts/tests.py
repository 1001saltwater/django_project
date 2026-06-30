from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileTests(APITestCase):

    def setUp(self):
        # 创建测试用户
        self.user = User.objects.create_user(
            username="testuser",
            password="123456"
        )

        # 创建 Profile
        self.profile = UserProfile.objects.create(
            user=self.user,
            nickname="CoffeeBird"
        )

    def test_get_profile(self):
        # 模拟登录
        self.client.force_authenticate(user=self.user)

        response = self.client.get("/api/profile/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["nickname"],
            "CoffeeBird"
        )

    def test_patch_profile(self):

        # 模拟登录
        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            "/api/profile/",
            {"nickname": "New CoffeeBird1"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["nickname"],
            "New CoffeeBird1"
        )

    def test_invalid_patch(self):

        # 模拟登录
        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            "/api/profile/",
            {"nickname": ""}
        )

        self.assertEqual(response.status_code, 400)

    def test_put_profile(self):

        # 模拟登录
        self.client.force_authenticate(user=self.user)

        response = self.client.put(
            "/api/profile/",
            {"nickname": "New CoffeeBird2"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["nickname"],
            "New CoffeeBird2"
        )

    def test_anonymous_cannot_get_profile(self):

        response = self.client.get("/api/profile/")

        self.assertEqual(response.status_code, 401)