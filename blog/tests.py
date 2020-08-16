from django.test import TestCase
from .models import CVSection

# These tests are now done in the functional tests - the response requires the user to be logged in so these tests no longer work here
# class BasicCVTest(TestCase):

#     def test_cv_returns_correct_template(self):
#         response = self.client.get('cv/')
#         self.assertTemplateUsed(response, 'cvtemplates/cv_view.html')

#     def test_profile_edit_returns_correct_html(self):
#         response = self.client.get('cv/edit/profile/')
#         self.assertTemplateUsed(response, 'cvtemplates/cv_edit.html')


class CVSectionModelTest(TestCase):

    def test_can_save_cv_sections(self):
        first_item = CVSection()
        first_item.section_name = 'A'
        first_item.text = 'First CV Section'
        first_item.save()

        second_item = CVSection()
        second_item.section_name = 'B'
        second_item.text = 'Second CV Section'
        second_item.save()

        saved_items = CVSection.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'First CV Section')
        self.assertEqual(second_saved_item.text, 'Second CV Section')

    # Further CV testing has been moved to the functional tests as they all require the user to be logged in, which is easier when using webdriver
