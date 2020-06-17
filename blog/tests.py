from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import post_list


class BasicCVTest(TestCase):

    def test_cv_returns_correct_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cvtemplates/cv_view.html')

