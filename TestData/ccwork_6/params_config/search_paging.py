"""
点击搜索后分页菜单 比如点击找人 找群后的搜索页面
"""
import time
from hamcrest import *
from selenium.webdriver.common.by import By
from TestData.ccwork_6.tools.baseOpera import BaseOpera
from TestData.ccwork_6.params_config.config_page import Config_page


class Search_Paging(Config_page):
    _search=(By.XPATH,"//*[@resource-id='com.kook.im:id/et_search']")
    _return1=(By.XPATH,"//*[@resource-id='com.kook.im:id/img_back']")
    _return2 = (By.XPATH, "//android.widget.ImageButton")
    _quxiao= (By.ID,"com.kook.im:id/txt_cancel")
    def search(self):
        self.find_element_and_sendkeys(self._search,sendkeys="123")
        time.sleep(3)
        self.find_element_and_sendkeys(self._search, sendkeys="1")
        assert self.driver.find_element_by_xpath("//*[@text='pytest_test1']").is_displayed()
        print("_______断言_______页面上输入1能够找到   pytest_test1 ")
        self.driver.find_element_by_xpath("//*[@text='pytest_test1']").click()
        time.sleep(2)
        self.find_element_and_click(self._return2)
        # //*[@text="pytest_test1"]
        self.find_element_and_sendkeys(self._search, sendkeys="交")
        assert self.driver.find_element_by_xpath("//*[@text='可交互式部门1-成员1']").is_displayed()
        driver = self.driver
        bo = BaseOpera(driver)
        bo.swipe_to_top()
        time.sleep(2)
        bo.swipe_to_bottom()
        time.sleep(2)
        self.find_element_and_click(self._return1)
        self.find_element_and_click(self._quxiao)
        return Search_Paging(self.driver)


    def search2(self):
        self.find_element_and_sendkeys(self._search, sendkeys="88877")
        time.sleep(2)
        self.find_element_and_click(self._return1)
        self.find_element_and_click(self._quxiao)

    def search3(self):
        self.find_element_and_sendkeys(self._search, sendkeys="第三次")
        time.sleep(2)

    def ret(self):
        self.find_element_and_click(self._return1)
