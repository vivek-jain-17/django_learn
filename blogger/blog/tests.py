from django.test import TestCase
from .models import BlogPost
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
class BlogPostTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            email="test@gmail.com",
            password = "testpassword",
        )
        cls.post = BlogPost.objects.create(
            title = "test post",
            body = "this is a test body",
            author = cls.user
        )
    
    def test_blogpost_model(self):
        self.assertEqual(self.post.title, "test post")
        self.assertEqual(self.post.body, "this is a test body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "test post")
        self.assertEqual(self.post.get_absolute_url(),"/post/1/")

    def test_url_exists_at_current_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_t_current_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertAlmostEqual(response.status_code, 200)
    
    def test_listview_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogpost_list.html")
        self.assertContains(response, "this is a test body")
    
    def test_detailview_page(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk":self.post.pk}))
        no_response = self.client.get("post/10000000/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "this is a test body")
        self.assertEqual(no_response.status_code, 404)   

    def test_create_post(self):
        response = self.client.post(
            reverse("post_create"),
            {
                "title":"new post",
                "body":"this is a new post body",
                "author": self.user.id
            },
        )            
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, "new post")
        self.assertEqual(BlogPost.objects.last().body, "this is a new post body")
        
    def test_upate_post(self):
        response = self.client.post(
            reverse("post_update", args=["1"]),
            {
                "title": "updated post",
                "body": "updated body",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, "updated post")
        self.assertEqual(BlogPost.objects.last().body, "updated body")
            
    def test_delete_post(self):
        response = self.client.post(reverse("post_delete", args = "1"))
        self.assertEqual(response.status_code, 302)