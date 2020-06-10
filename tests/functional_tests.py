from selenium import webdriver
import unittest


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_browser_title_correct(self):

        self.browser.get('http://localhost:8000/cv')

        self.assertIn('Ciaran', self.browser.title)



        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
