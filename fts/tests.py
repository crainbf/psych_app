from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TrialParticipationTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_complete_experiment(self):
        # Barbie opens her web browser and goes to the disclaimer page
        self.browser.get(self.live_server_url + '/disclaimer/')

        # She sees the header 'Stroop Task - Disclaimer'
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Stroop - Disclaimer', body)

        # She sees the button 'I shall consent' and clicks on it

        # She is taken to a new page with the headline 'Instructions'

        # She sees a checkbox that says 'I understand'

        # She checks the checkbox

        # She sees a button saying 'Start Practice Session' and clicks it

        # She sees the headline 'Stroop Task Practice Session'

        # She sees the text practice trial '1 out of 10'

        # She is taken to the main experiment page and sees the headlin
        # 'Simple Stroop Task Experiment'
        self.fail('Not yet...')


class AdminFunctionalTest(LiveServerTestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_log_into_admin_site_TrialResponse_displaying(self):
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

        # He clicks on the 'Trial responses' link
        trialresponse_link = self.browser.find_element_by_link_text('Trial responses')
        trialresponse_link.click()

        # He sees the the tabs for 'Participant id', 'Session number' and 'Reaction time'
        body = self.browser.find_element_by_tag_name('body')
        self.browser.implicitly_wait(3)
        self.assertIn('Participant id', body.text)
        self.assertIn('Session number', body.text)
        self.assertIn('Reaction time', body.text)

        self.fail('Success!!')


