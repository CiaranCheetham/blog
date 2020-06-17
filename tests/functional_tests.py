from selenium import webdriver
import unittest


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    # def tearDown(self):
    #     self.browser.quit()

    def test_can_view_and_edit_cv(self):

        # Ciaran wants to view and edit his CV - he visits the web page
        self.browser.get('http://localhost:8000/cv')

        # The title of the web page shows his name
        # He recognises the page as the CV page
        self.assertIn('Ciaran Cheetham', self.browser.title)
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('CV', body_text)

        # He reads his CV and wants to edit his "experience" section by pressing the neighbouring button
        self.assertIn('Experience', body_text)
        exp_edit_btn = self.browser.find_element_by_class_name('exp_edit')
        exp_edit_btn.click()

        # Do I also need to test every other button?? Probably, but does it need to be here or as a unit test?


        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
