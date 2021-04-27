
"""
 账号登陆之后进入的工作页面   消息  通讯录  工作台  我的
"""
import time

from selenium.webdriver.common.by import By

from TestData.ccwork_6.params_config.config_page import Config_page
from TestData.ccwork_6.params_config.news.news import News
from TestData.ccwork_6.params_config.news.more_options import More


class Work_Kanban(Config_page):
    #消息
    _news=(By.XPATH,"//*[@resource-id='android:id/tabs']/android.widget.FrameLayout[1]")
    _more = (By.XPATH, "//*[@content-desc='更多选项']")


    # def kanban_MySchedule(self):  # 看板——我的日程
    #     pass
    #
    # def kanban_MyTask(self):  # 看板——我的任务
    #     pass
    #
    # def kanban_Agency(self):  # 看板——统一代办
    #     pass
    #
    # def apply(self):  # 应用
    #     pass

    def news(self): # 消息
        self.find_element_and_click(self._news)
        return News(self.driver)

    def more_options(self):# 更多选项
        self.find_element_and_click(self._more)
        return More(self.driver)



