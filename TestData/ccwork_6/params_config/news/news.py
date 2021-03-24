

"""
主页面-消息页面
"""
from selenium.webdriver.common.by import By
from TestData.ccwork_6.params_config.config_page import Config_page
from TestData.ccwork_6.params_config.search import To_Search


class News(Config_page):
    _search=(By.XPATH,"//*[@content-desc='搜索']")

    def news(self):
        pass


    def search(self):
        self.find_element_and_click(self._search)
        return To_Search(self.driver)