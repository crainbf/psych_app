from django.test import LiveServerTestCase
from selenium import webdriver


class AdminFunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_admin_site_is_displaying(self):
        #Mark opens his web browser and goes to the admin page
        self.browser.get(self.live_server_url + '/admin/')

        #He sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)
