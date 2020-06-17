from django.test import TestCase


class BasicCVTest(TestCase):

    def test_cv_returns_correct_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cvtemplates/cv_view.html')

    def test_exp_edit_returns_correct_html(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'cvtemplates/cv_edit.html')
