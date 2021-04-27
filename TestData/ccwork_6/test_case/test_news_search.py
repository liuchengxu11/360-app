
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

    @pytest.fixture()
    def news(self):
        self.new1 = self.lg

    def setup_class(self):# 登陆后点击消息  在点击消息页面上方的搜索按钮
        # self.lg=App.app().login_er().login()
        self.lg = App.app().login()
        time.sleep(3)

    @pytest.mark.run(order=1)
    def test_search_people(self,search):  # 在消息 搜索中心的总目录 选择找人
        self.found = self.search_page.people()
        self.found.search()
        print("test_search_people-------------------")

    @pytest.mark.run(order=2)
    def test_create_grep(self,news):  # 在消息  点击更多 创建群聊
        self.more = self.new1.more_options().grep_page()
        self.more.my_dept()



    @pytest.mark.run(order=3)
    def test_search_grep(self,search):  #  在消息  搜索中心的总目录 选择找群
        self.found = self.search_page.group()
        self.found.search2()






    def teardown_class(self):
        App.quit()










