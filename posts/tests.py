from django.test import TestCase

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