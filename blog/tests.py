from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import post_list


class HomeTest(TestCase):

    def test_post_list_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

