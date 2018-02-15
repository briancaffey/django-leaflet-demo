from django.test import LiveServerTestCase
from selenium import webdriver

class NewUserTest(LiveServerTestCase):
    def setUp(self):
        self.b = webdriver.Firefox()
    
    def tearDown(self):
        self.b.quit()

    def test_nothing(self):
        self.assertTrue(1==1)