"""
登陆账号密码输入环节
"""
import time

from selenium.webdriver.common.by import By

from TestData.ccwork_6.params_config.work_kanban.work_kanban import Work_Kanban
from TestData.ccwork_6.params_config.config_page import Config_page


class Signup(Config_page):
    _accout = (By.ID, "com.kook.im:id/et_accout")
    _password = (By.ID, "com.kook.im:id/et_password")
    _ip = (By.ID, "com.kook.im:id/et_ip")
    _batton = (By.ID, "com.kook.im:id/btn_login")
    _error = (By.XPATH, "//*[@resource-id='com.kook.im:id/txt_left']")

    def login(self):
        # 账号，密码，登陆
        self.find_element_and_sendkeys(self._accout, "pytest_test1")
        self.find_element_and_sendkeys(self._password, "Liu123123")
        self.find_element_and_sendkeys(self._ip, "10.206.83.102:8282")
        self.find_element_and_click(self._batton)

        return Work_Kanban(self.driver)  # 进入工作看板页面

    def login_er(self):
        # 测试异常情况下的账号密码输入
        self.find_element_and_sendkeys(self._accout, "pytest_test1")
        self.find_element_and_sendkeys(self._password, "121212")
        self.find_element_and_sendkeys(self._ip, "10.206.83.102:8282")
        self.find_element_and_click(self._batton)
        time.sleep(3)
        self.find_element_and_click(self._error)

        self.find_element_and_sendkeys(self._accout, "_test1")
        self.find_element_and_sendkeys(self._password, "Liu123123")
        self.find_element_and_sendkeys(self._ip, "10.206.83.102:8282")
        self.find_element_and_click(self._batton)
        time.sleep(3)
        self.find_element_and_click(self._error)

        self.find_element_and_sendkeys(self._accout, "pytest_test1")
        self.find_element_and_sendkeys(self._password, "Liu123123")
        self.find_element_and_sendkeys(self._ip, "10.206.83.122:8282")
        self.find_element_and_click(self._batton)
        time.sleep(3)
        self.find_element_and_click(self._error)

        return Signup(self.driver)
