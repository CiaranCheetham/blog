from django.test import TestCase
from .models import CVSection


class BasicCVTest(TestCase):

    def test_cv_returns_correct_template(self):
        response = self.client.get('cv/')
        self.assertTemplateUsed(response, 'cvtemplates/cv_view.html')

    def test_exp_edit_returns_correct_html(self):
        response = self.client.get('cv/edit/profile/')
        self.assertTemplateUsed(response, 'cvtemplates/cv_edit.html')


class CVSectionModelTest(TestCase):

    def test_can_save_cv_sections(self):
        first_item = CVSection()
        first_item.text = 'First CV Section'
        first_item.save()

        second_item = CVSection()
        second_item.text = 'Second CV Section'
        second_item.save()

        saved_items = CVSection.objects.all()
        saved_items_text = saved_items.map(lambda item : item.text)

        self.assertIsIn(first_item.text, saved_items_text)
        self.assertIsIn(second_item.text, saved_items_text)
