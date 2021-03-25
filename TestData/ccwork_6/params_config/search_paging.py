"""
点击搜索后分页菜单 比如点击找人 找群后的搜索页面
"""
import time
from hamcrest import *
from selenium.webdriver.common.by import By

from TestData.ccwork_6.params_config.config_page import Config_page

class Search_Paging(Config_page):
    _search=(By.XPATH,"//*[@resource-id='com.kook.im:id/et_search']")
    _return1=(By.XPATH,"//android.widget.ImageButton")

    def search(self):
        self.find_element_and_sendkeys(self._search,sendkeys="123")
        time.sleep(3)
        self.find_element_and_sendkeys(self._search, sendkeys="1")
        # //*[@text="pytest_test1"]



    def return1(self):
        pass