# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from conacts import Contacts

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contacts(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def login(self, wd, user, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def add_new_contact(self, wd, contacts):
        # add new contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
    
    def test_add_contacts(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user="admin", password="secret")
        self.add_new_contact(wd, Contacts(firstname="Ekaterina", lastname="Samoilova", nickname="eksam", title="123", company="Ek and Co", email="esamoilova@mail.ru"))
        self.logout(wd)

    def test_add_two_contacts(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, user="admin", password="secret")
        self.add_new_contact(wd, Contacts(firstname="Ivan", lastname="Petrov", nickname="ivaN", title="luxry", company="VIPcomp", email="VIOiva123@mail.ru"))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
