from django.test import LiveServerTestCase
from selenium import webdriver
import time

class NewUserTest(LiveServerTestCase):
    def setUp(self):
        self.b = webdriver.Firefox()
        self.domain = "http://127.0.0.1:8081"
    
    def tearDown(self):
        self.b.quit()
        
    def test_register_new_user(self):
        self.b.get(self.domain + '/accounts/register')
        html = self.b.page_source
        self.assertIn('Register', html)
        self.b.find_element_by_id('id_username').send_keys('jim')
        self.b.find_element_by_id('id_email').send_keys('briancaffey2010@gmail.com')
        self.b.find_element_by_id('id_confirm_email').send_keys('briancaffey2010@gmail.com')
        self.b.find_element_by_id('id_first_name').send_keys('Brian')
        self.b.find_element_by_id('id_last_name').send_keys('Caffey')
        self.b.find_element_by_id('id_password').send_keys('qwer1234')
        self.b.find_element_by_id('id_submit').click()
        html = self.b.page_source
        self.assertNotIn('Register', html)