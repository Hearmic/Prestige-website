from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from users.forms import LoginUserForm

class LoginUserViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('users:login')

    def test_login_form_renders_with_empty_form_when_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], LoginUserForm)
        self.assertFalse(response.context['form'].is_bound)

    def test_login_form_renders_with_empty_form_when_post_request_without_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], LoginUserForm)
        self.assertFalse(response.context['form'].is_valid())
        self.assertFalse(response.context['form'].is_bound)

    def test_login_form_renders_with_empty_form_when_post_request_with_invalid_data(self):
        response = self.client.post(self.url, {'username': 'invalid', 'password': 'invalid'})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], LoginUserForm)
        self.assertFalse(response.context['form'].is_valid())
        self.assertTrue(response.context['form'].is_bound)

    def test_login_form_redirects_to_home_page_when_post_request_with_valid_data(self):
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('main:home'))

    def test_login_form_does_not_redirect_when_post_request_with_invalid_data(self):
        response = self.client.post(self.url, {'username': 'invalid', 'password': 'invalid'})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('main:home', response.url)