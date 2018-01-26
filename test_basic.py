from pagefactory_support import cacheable, callable_find_by
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(TestCase):

    def setUp(self):
        path = "C:\\Users\\LLenk\\Downloads\\chromedriver_win32\\chromedriver.exe"
        self.driver = webdriver.Chrome(path)

    def test_search_in_python(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


class LoginTests(TestCase):

    def setUp(self):
        path = "C:\\Users\\LLenk\\Downloads\\chromedriver_win32\\chromedriver.exe"
        self.driver = webdriver.Chrome(path)

    def test_basic_login_cactus_5(self):
        """Basic happy path test of the login"""
        driver = self.driver
        driver.get("http://ctc-qa-app2k16:83/web-external/")
        LoginPage.enter_username()
        LoginPage.enter_password()
        LoginPage.click_login_btn()

    def tearDown(self):
        self.driver.close()


class LoginPage(object):

    _logIn = callable_find_by(id_="login_button")
    _userId = callable_find_by(id_="username_textfield")
    _password = callable_find_by(id_="password_textfield")
    _noUsernameValidationMsg = callable_find_by(
        xpath="//div[@class='help-block' and text()='Username is required']")
    _noPasswordValidationMsg = callable_find_by(
        xpath="//div[@class='help-block' and text()='Password is required']")
    _parent_xpath = ".."

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username="CTC"):
        self._userId().send_keys(username)

    def enter_password(self, password="CTC45402"):
        self._password().send_keys(password)

    def click_login_btn(self):
        self._logIn().click()

    def is_no_username_validation_msg_displayed(self):
        is_msg_displayed = False
        parent = self._noUsernameValidationMsg().find_element(By.XPATH(self._parent_xpath))
        classes = parent.get_attribute("class")
        if "has error" in classes:
            is_msg_displayed = True
        return is_msg_displayed

    def is_no_password_validation_msg_displayed(self):
        is_msg_displayed = False
        parent = self._noPasswordValidationMsg().find_element(By.XPATH(self._parent_xpath))
        classes = parent.get_attribute("class")
        if "has error" in classes:
            is_msg_displayed = True
        return is_msg_displayed
