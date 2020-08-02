from selenium import webdriver
import unittest
import time


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_and_edit_cv_when_logged_in(self):

        # Ciaran wants to view and edit his CV - he visits his web page and logs in
        self.browser.get('http://localhost:8000/')
        login_btn = self.browser.find_element_by_class_name('top-menu')
        login_btn.click()
        user_field = self.browser.find_element_by_id('id_username')
        user_field.send_keys('ciaran')
        pswd_btn = self.browser.find_element_by_id('id_password')
        pswd_btn.send_keys('testpassword')
        time.sleep(2)
        submit_btn = self.browser.find_element_by_xpath("//input[@type='submit']")
        submit_btn.click()

        # He is redirected to the home page
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/')

        # He recognises and presses the CV button at the top of the page
        cv_btn = self.browser.find_element_by_link_text('CV')
        cv_btn.click()
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/')

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

        # He now wants to edit his profile section to say "This is my profile".
        # After clicking the button he is brought to the page to edit his profile section
        profile_edit_btn = self.browser.find_element_by_class_name('profile')
        profile_edit_btn.click()
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/edit/profile/')
        edit_box = self.browser.find_element_by_tag_name('textarea')
        edit_box.clear()
        edit_box.send_keys('This is my profile')
        save_btn = self.browser.find_element_by_tag_name('button')
        save_btn.click()

        # He is redirected to the CV page, where he sees that the 'profile' section has been updated
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/')
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('This is my profile', body_text)

        # He now wants to edit his education section to say "This is my education"
        # After clicking the button he is brought to the page to edit his education section
        education_edit_btn = self.browser.find_element_by_class_name('education')
        education_edit_btn.click()
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/edit/education/')
        edit_box = self.browser.find_element_by_tag_name('textarea')
        edit_box.clear()
        edit_box.send_keys('This is my education')
        save_btn = self.browser.find_element_by_tag_name('button')
        save_btn.click()

        # He is redirected to the CV page, where he sees that the 'education' section has been updated
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/')
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('This is my education', body_text)

        # He now wants to edit his projects section to say "These are my projects"
        # After clicking the button he is brought to the page to edit his projects section
        projects_edit_btn = self.browser.find_element_by_class_name('projects')
        projects_edit_btn.click()
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/edit/projects/')
        edit_box = self.browser.find_element_by_tag_name('textarea')
        edit_box.clear()
        edit_box.send_keys('These are my projects')
        save_btn = self.browser.find_element_by_tag_name('button')
        save_btn.click()

        # He is redirected to the CV page, where he sees that the 'projects' section has been updated
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/')
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('These are my projects', body_text)

        # Finally, he now wants to edit his achievements & interests section to say "These are my interests"
        # After clicking the button he is brought to the page to edit his interests section
        interests_edit_btn = self.browser.find_element_by_class_name('interests')
        interests_edit_btn.click()
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/edit/interests/')
        edit_box = self.browser.find_element_by_tag_name('textarea')
        edit_box.clear()
        edit_box.send_keys('These are my interests')
        save_btn = self.browser.find_element_by_tag_name('button')
        save_btn.click()

        # He is redirected to the CV page, where he sees that the 'achievements & interests' section has been updated
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/')
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('These are my interests', body_text)

    def test_cannot_edit_cv_when_not_logged_in(self):

        # A local ne'er do well wants to edit Ciaran's CV without his permission
        # He goes to the CV page by pressing the CV button
        self.browser.get('http://localhost:8000/')
        cv_btn = self.browser.find_element_by_link_text('CV')
        cv_btn.click()
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/cv/')

        # He sees that there are no buttons he can press which would allow him to edit the CV
        edit_btn_names = ['profile', 'exp', 'education', 'interests', 'projects']
        for btn_name in edit_btn_names:
            try:
                self.browser.find_element_by_class_name(btn_name)
                self.fail()
            except:
                pass

        # He attempts to edit the page by going directly to a URL he suspects will grant him access
        self.browser.get('http://localhost:8000/cv/edit/profile/')

        # He is greeted with the login screen, and realises he cannot edit the CV without being logged in
        self.assertEqual(self.browser.current_url, 'http://localhost:8000/accounts/login/?next=/cv/edit/profile/')


if __name__ == '__main__':
    unittest.main()
