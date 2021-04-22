
"""
消息以及组织架构上方的搜索框
"""
import time

from selenium.webdriver.common.by import By

from TestData.ccwork_6.params_config.config_page import Config_page
from TestData.ccwork_6.params_config.search_paging import Search_Paging
from TestData.ccwork_6.tools.baseOpera import BaseOpera


class To_Search(Config_page):
    _people=(By.XPATH,"//*[@text='找人']")
    _grep=(By.XPATH,"//*[@text='群聊']")
    _record=(By.XPATH,"//*[@text='聊天记录']")

    def people(self):  # 找人
        time.sleep(5)
        self.find_element_and_click(self._people)
        return Search_Paging(self.driver)

    def group(self):  # 找群
        time.sleep(5)
        self.find_element_and_click(self._grep)
        return Search_Paging(self.driver)

    def apply(self):  # 应用
        pass

    def apply_news(self):  # 应用消息
        pass

    def chat_record(self):  # 聊天记录
        pass




