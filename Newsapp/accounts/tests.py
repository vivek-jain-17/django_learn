from django.test import TestCase
from django.contrib.auth import get_user_model
from  django.urls import reverse
# Create your tests here.
class ManageUserTest(TestCase):
    def test_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email = "test@gmail.com",
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            username='testuser',
            password='testpassword',
            email = "test@gmail.com",
        )    
        self.assertEqual(super_user.username, 'testuser')
        self.assertEqual(super_user.email, 'test@gmail.com')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)


class SignUpPageTests(TestCase):
    def test_signup_page_exists(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_page_exists_by_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("registration/signup.html")
        
    def test_signup_form(self):
        response = self.client.post(reverse("signup"),
            {
                "username":"testuser",
                "email":"test@email.com",
                "age":17,
                "password1":"testpass123@",
                "password2":"testpass123@",
            },
            )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "test@email.com")
        self.assertEqual(get_user_model().objects.all()[0].age, 17)

            