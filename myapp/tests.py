from django.test import TestCase
from django.urls import reverse


class ApiTests(TestCase):
    def test_api_returns_success(self):
        response = self.client.get(reverse("hello_api"))
        self.assertEqual(response.status_code, 200)

    def test_api_returns_expected_message(self):
        response = self.client.get(reverse("hello_api"))
        self.assertEqual(
            response.json(),
            {
                "message": "Hello from Kevin's API!",
                "course": "CSC325",
            },
        )