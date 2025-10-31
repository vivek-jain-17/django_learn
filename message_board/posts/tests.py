from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.
class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="this is a Text")

    def test_model_content(self):
        self.assertEqual(self.post.text, "this is a Text")

    def test_url_exists_at_current_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("postlist"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "this is a Text")
        self.assertTemplateUsed(response,"post_list.html")
    