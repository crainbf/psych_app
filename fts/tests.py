from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AdminFunctionalTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_log_into_admin_site_is_displaying(self):
        # Mark opens his web browser and goes to the admin page
        self.browser.get(self.live_server_url + '/admin/')

        # He sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # Mark types username and password and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('pass')
        password_field.send_keys(Keys.RETURN)

        # Can see the Trial Response objects
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Trial responses', body.text)
