from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.urls import reverse
import os
import socket


class PinpointTests(StaticLiveServerTestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options = chrome_options)
        self.browser.implicitly_wait(3)

    @classmethod
    def setUpClass(cls):
        cls.host = socket.gethostbyname(socket.gethostname())
        super(PinpointTests, cls).setUpClass()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_navigate_from_home_to_quiz(self):
        # Go to pinpoint home page
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        print(url)
        self.browser.get(url + reverse('home'))

        # Search for a link to About page
        about_link = self.browser.find_element_by_partial_link_text("Quiz")
        about_link.click()

        # Check if it goes back to the home page
        self.assertIn(url + reverse('quiz'), self.browser.current_url)

    def test_navigate_from_quiz_to_home(self):
        # Go to rango main page
        self.client.get(reverse('home'))
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('quiz'))

        # Check if there is a link back to the home page
        # link_to_home_page = self.browser.find_element_by_tag_name('a')
        link_to_home_page = self.browser.find_element_by_link_text('Home')
        link_to_home_page.click()

        # Check if it goes back to the home page
        self.assertEqual(url + reverse('home'), self.browser.current_url)


