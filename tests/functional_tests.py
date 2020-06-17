from selenium import webdriver
import unittest


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_and_edit_cv(self):

        # Ciaran wants to view and edit his CV - he visits the web page
        self.browser.get('http://localhost:8000/cv')

        # He recognises and presses the CV button at the top of the page

        # The title of the web page shows his name
        # He recognises the page as the CV page
        self.assertIn('Ciaran Cheetham', self.browser.title)
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('CV', body_text)

        # He reads his CV and wants to edit his "experience" section by pressing the neighbouring button
        self.assertIn('Experience', body_text)
        exp_edit_btn = self.browser.find_element_by_class_name('exp')
        exp_edit_btn.click()
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/edit/exp/')

        # He is greeted by a form filled with the current text for the experience section
        edit_box = self.browser.find_element_by_tag_name('textarea')
        self.assertIsNotNone(edit_box.text)

        # He changes the form to just say "This is my experience" and presses save
        edit_box.clear()
        edit_box.send_keys('This is my experience')
        save_btn = self.browser.find_element_by_tag_name('button')
        save_btn.click()

        # He is redirected to the CV page, where he sees that the 'experience' section has been updated
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/')
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('This is my experience', body_text)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
