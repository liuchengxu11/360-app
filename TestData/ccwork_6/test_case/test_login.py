
"""

登陆
"""
import time
import pytest
from TestData.ccwork_6.params_config.app import App


class Test_log:

    def setup(self):# 登陆后点击消息  在点击消息页面上方的搜索按钮
        self.news=App.app().news()
        self.search_page=self.news.search()



    def test_search_people(self):  # 在消息 搜索中心的总目录 选择找人
        self.found = self.search_page.people()
        self.found.search()

    def teardown(self):
        App.quit()



