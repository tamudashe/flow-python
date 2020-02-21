from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client, TestCase  #  Client: used for testing views
from django.urls import reverse

from .models import Post

# Create your tests here.
class InternshipTests(TestCase):
    def set_up(self):
        self.post = Post.objects.create(
            company_name = 'test company',
            title = 'test title',
            location = 'test state',
            classification = 'year in school',
            application_link = 'test url'
        )
    
    def test_string_representations(self):
        post = Post(title='test title')
        self.assertEqual(str(post), post.title)
    
    def test_post_list_view(self):
        response = self.client.get(reverse('internships'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'internships.html')
