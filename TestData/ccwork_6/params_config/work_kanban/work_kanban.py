
"""
 账号登陆之后进入的工作台页面
"""
from selenium.webdriver.common.by import By

from TestData.ccwork_6.params_config.config_page import Config_page
from TestData.ccwork_6.params_config.news.news import News


class Work_Kanban(Config_page):
    _news=(By.XPATH,"//*[@resource-id='android:id/tabs']/android.widget.FrameLayout[2]")

    def kanban_MySchedule(self):  # 看板——我的日程
        pass

    def kanban_MyTask(self):  # 看板——我的任务
        pass

    def kanban_Agency(self):  # 看板——统一代办
        pass

    def apply(self):  # 应用
        pass

    def news(self): # 消息
        self.find_element_and_click(self._news)
        return News(self.driver)

    def kanban(self):  # 看板

        pass

    def organization(self):  # 组织架构
        pass

    def my(self):  # 我的
        pass
