"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve
from website.views import home, disclaimer
from django.http import HttpRequest


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_disclaimer_returns_correct_html(self):
        request = HttpRequest()
        response = disclaimer(request)
        self.assertTrue(response.content.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Stroop Task - Disclaimer</title>', response.content)
        self.assertIn('If you agree with the conditions', response.content)
        self.assertIn("<input type='submit' value='I shall consent'>", response.content)
        self.assertTrue(response.content.endswith('</html>'))

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        self.assertTrue(response.content.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Simple Stroop Task</title>', response.content)
        self.assertTrue(response.content.endswith('</html>'))
