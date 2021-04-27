import time

import pytest
from selenium.webdriver.common.by import By

from TestData.ccwork_6.params_config.config_page import Config_page
"""
消息页面 点击更多  发起群聊 后




"""

class Grep_Page(Config_page):
    _my_dept=(By.XPATH,"//*[@resource-id='com.kook.im:id/ll_my_group']")
    _back=(By.XPATH,"//android.widget.ImageButton")

    # @pytest.fixture()
    # def back_off(self):
    #     yield
    #     self.find_element_and_click(self._back)
    #     self.find_element_and_click(self._back)

    def my_dept(self):
        self.find_element_and_click(self._my_dept)
        time.sleep(3)
        self.find_element_and_click(self._back)
        self.find_element_and_click(self._back)
