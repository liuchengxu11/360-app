import time

import pytest
from selenium.webdriver.common.by import By

from TestData.ccwork_6.params_config.config_page import Config_page
from TestData.ccwork_6.params_config.news.create_grep.grep_page import Grep_Page


"""
消息页面  点击更多   创建群   创建任务   创建日程  扫一扫
"""

class More(Config_page):
    _grep=(By.XPATH,"//*[@text='发起群聊']")
    _dept=(By.XPATH,"//*[@text='我的部门']")
    _my_dept = (By.XPATH, "//*[@resource-id='com.kook.im:id/ll_my_group']")


    def grep_my_dept(self):
        self.find_element_and_click(self._grep)
        self.find_element_and_click(self._my_dept)
        return Grep_Page(self.driver)

    def grep_page(self):
        self.find_element_and_click(self._grep)
        return Grep_Page(self.driver)



