from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTests(TestCase):
    """Post Tests"""

    @classmethod
    def setUpTestData(cls):
        """Set up the data needed for each test"""
        cls.post = Post.objects.create(text = "This is a test!")

    def test_model_content(self):
        """Test the model content"""
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        """Test url exists at correct location"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        """Test the home page"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")