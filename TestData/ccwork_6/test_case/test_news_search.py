
"""

登陆后  消息模块的  搜索相关用例
"""
import time
import pytest
from TestData.ccwork_6.params_config.app import App
import commands


class Test_log:
    @pytest.fixture()
    def search(self):
        self.news = self.lg.news()
        self.search_page = self.news.search()

    def setup_class(self):# 登陆后点击消息  在点击消息页面上方的搜索按钮
        self.lg=App.app().login_er().login()
        time.sleep(3)
        # self.news=self.lg.news()
        # self.search_page=self.news.search()

    def test_search_people(self,search):  # 在消息 搜索中心的总目录 选择找人
        self.found = self.search_page.people()
        self.found.search()
        print("test_search_people-------------------")

    def test_search_grep(self,search):  #  在消息  搜索中心的总目录 选择找群
        self.found = self.search_page.group()
        self.found.search2()
        print("test_search_grep-------------------")



    def teardown_class(self):
        App.quit()










