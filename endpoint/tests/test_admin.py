from django.test import TestCase
from django.urls import reverse


class AdminViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('admin:login'))
        self.assertEqual(response.status_code, 200)
