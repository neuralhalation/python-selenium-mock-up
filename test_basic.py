from pagefactory_support import cacheable, callable_find_by
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class LoginTests(TestCase):

    def setUp(self):
        path = "/path/to/chromedriver.exe"
        self.driver = webdriver.Chrome(path)

    def test_basic_login_cactus_5(self):
        """Basic happy path test of the login"""
        driver = self.driver
        login_page = LoginPage(driver)
        select_entities_modal = SelectEntityModal(driver)
        driver.get("http://ctc-qa-app2k16:83/web-external/")

        login_page.enter_username("username")
        login_page.enter_password("password")
        login_page.click_login_btn()
        select_entities_modal.wait_for_modal_dialog(300)

        select_entities_modal.click_ok_button()

    def test_login_fails_with_no_creds(self):
        driver = self.driver
        login_page = LoginPage(driver)
        select_entities_modal = SelectEntityModal(driver)
        driver.get("http://ctc-qa-app2k16:83/web-external/")
        login_page.click_login_btn()

    def tearDown(self):
        self.driver.close()


class Form(object):
    _entityHeader = callable_find_by(xpath="//div[@class='entity']")
    _header = callable_find_by(xpath="//div[@class='section-header']/h1'")
    _home = callable_find_by(xpath="//a[@routerlink='cactus/home']")
    _dashboard = callable_find_by(
        xpath="//a[@routerlink='cactus/dashboard']")
    _tasks = callable_find_by(xpath="a[@routerlink='cactus/tasks']")
    _inbox = callable_find_by(
        xpath="//a[@routerlink='cactus/inbox']")
    _system = callable_find_by(
        xpath="//a[@routerlink='cactus/system-settings']")
    _searchButton = callable_find_by(id_="search_button")
    _searchTextBox = callable_find_by(id_="globalSearch_textfield")
    _providerSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/providers']")
    _formSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/forms']")
    _queriesSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/queries']")
    _documentSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/documents']")
    _reportsSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/reports']")
    _profilesSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/profiles']")
    _packetsSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/packets']")
    _referenceListSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/referencelists']")
    _systemFormsSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/systemforms']")
    _groupsSeachOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/groups']")
    _formbankSearchOption = callable_find_by(
        xpath="//li[@data-redirect='cactus/searchresults/formbank']")
    _quickLaunchContainer = "//div[@class='quick-launch']"
    _quickLaunchDdl = callable_find_by(
        xpath="//div[@class='quick-launch']/div[contains(2class, 'dropdown')]")
    _quickLaunchHideButton = callable_find_by(
        xpath="//div[@class='hide-menu']")
    _spinner = callable_find_by(class_name="spinner_icon")

    # bottom toolbar

    _newLink = callable_find_by(id_="newToolbar_link")
    _saveLink = callable_find_by(id_="saveToolbar_link")
    _searchLink = callable_find_by(id_="searchToolbar_link")
    _refreshLink = callable_find_by(id_="refreshToolbar_link")
    _runLink = callable_find_by(id_="runToolbar_link")
    _deleteLink = callable_find_by(id_="deleteToolbar_link")
    _firstElementLink = callable_find_by(id_="firstElementToolbar_link")
    _moveBackLink = callable_find_by(id_="moveBackToolbar_link")
    _mainGridLink = callable_find_by(id_="mainGridToolbar_link")
    _moveForwardLink = callable_find_by(id_="moveForward_link")
    _lastElementLink = callable_find_by(id_="lastElementToolbar_link")
    _pinBtn = callable_find_by(id_="pinToolbar_link")
    _tasksBtn = callable_find_by(id_="tasksToolbar_link")
    _imagesBtn = callable_find_by(id_="imagesToolbar_link")
    _notesBtn = callable_find_by(id_="notesToolbar_link")
    _adminBtn = callable_find_by(id_="adminToolbar_link")

    def click_home(self):
        self._home().click()

    def click_dashboard(self):
        self._dashboard().click()

    def click_tasks(self):
        self._tasks().click()

    def click_inbox(self):
        self._inbox().click()

    def click_system(self):
        self._system().click()

    def click_search_btn(self):
        self._searchButton().click()

    def enter_search_text(self, text):
        self._searchTextBox().send_keys(text)

    def click_provider_search_btn(self):
        self._profilesSearchOption().click()

    def click_form_search_btn(self):
        self._formSearchOption().click()

    def click_queries_search_btn(self):
        self._queriesSearchOption().click()

    def click_document_search_btn(self):
        self._documentSearchOption().click()

    def click_reports_search_btn(self):
        self._reportsSearchOption().click()

    def click_profiles_search_btn(self):
        self._profilesSearchOption().click()

    def click_packets_search_btn(self):
        self._packetsSearchOption().click()

    def click_reference_list_search_btn(self):
        self._referenceListSearchOption().click()

    def click_system_forms_search_btn(self):
        self._groupsSeachOption().click()

    def click_form_bank_search_btn(self):
        self._formbankSearchOption().click()

    def click_quick_launch_hide_btn(self):
        self._quickLaunchHideButton().click()

    def click_new_link(self):
        self._newLink().click()

    def click_save_link(self):
        self._saveLink().click()

    def click_search_link(self):
        self._searchLink().click()

    def click_refresh_link(self):
        self._refreshLink().click()

    def click_run_link(self):
        self._runLink().click()

    def click_delete_link(self):
        self._deleteLink().click()

    def click_first_element_link(self):
        self._firstElementLink().click()

    def click_move_back_link(self):
        self._moveBackLink().click()

    def click_main_grid_link(self):
        self._mainGridLink().click()

    def click_move_forward_link(self):
        self._moveForwardLink().click()

    def click_last_element_link(self):
        self._lastElementLink().click()

    def click_pin_btn(self):
        self._pinBtn().click()

    def click_tasks_btn(self):
        self._tasksBtn().click()

    def click_images_btn(self):
        self._imagesBtn().click()

    def click_notes_btn(self):
        self._notesBtn().click()

    def click_admin_btn(self):
        self._adminBtn().click()


class LoginPage(Form):

    _logIn = callable_find_by(id_="login_button")
    _userId = callable_find_by(id_="username_textfield")
    _password = callable_find_by(id_="password_textfield")
    _noUsernameValidationMsg = callable_find_by(
        xpath="//div[@class='help-block' and text()='Username is required']")
    _noPasswordValidationMsg = callable_find_by(
        xpath="//div[@class='help-block' and text()='Password is required']")
    _parent_xpath = ".."

    def __init__(self, driver):
        self._driver = driver

    def enter_username(self, username="username"):
        self._userId().send_keys(username)

    def enter_password(self, password="password"):
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
        parent = self._noPasswordValidationMsg().find_element(
            By.XPATH(self._parent_xpath))
        classes = parent.get_attribute("class")
        if "has error" in classes:
            is_msg_displayed = True
        return is_msg_displayed


class Modal(object):
    _close_button = callable_find_by(
        xpath="//div[@class='modal-header']/button[@aria-label='Close']")
    _modal_label = callable_find_by(id_="exampleModalLabel")
    _ok_button = callable_find_by(
        xpath="//div[@class='modal-footer']/button[@id='ok_button']")
    _cancel_button = callable_find_by(
        xpath="//div[@class='modal-footer']/button[contains(., 'Cancel')]")
    _new_button = callable_find_by(
        xpath="//div[@class='modal-footer']/button/contains(., 'New')]")

    def __init__(self, driver):
        self._driver = driver

    def click_close_button(self):
        self._close_button().click()

    def click_ok_button(self):
        self._ok_button().click()

    def click_cancel_button(self):
        self._cancel_button().click()

    def click_new_button(self):
        self._new_button().click()

    def wait_for_modal_dialog(self, time_to_wait):
        try:
            elem = WebDriverWait(self._driver, time_to_wait).until(
                ec.presence_of_element_located((
                    By.XPATH,
                    "//div[@class='modal-footer']/button[@id='ok_button']")))
        except TimeoutException:
            print "Loading took too much time!"


class SelectEntityModal(Modal):
    _filter_entities_input = callable_find_by(id_="FilterEntities_input")
    _entity_selection_div = callable_find_by(id_="custom-multiselect")
    _default_entity = callable_find_by(
        xpath="//div[@class='custom-multiselect']/label/span[1]")
    _entity = callable_find_by(
        xpath="//div[@class='custom-multiselect']/label/span")

    def __init__(self, driver):
        self._driver = driver

    def enter_filter_entities_txtbx_text(self, text):
        self._filter_entities_input().send_keys(text)
