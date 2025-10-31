from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageviewTest(SimpleTestCase):
    def test_page_exist_at_given_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_page_exist_by_the_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("home.html")
        self.assertContains(response,"HOME")
