import os
import time

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from TestData.ccwork_6.params_config.work_kanban.work_kanban import Work_Kanban

"""
查找app包的命令 adb shell dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'

adb shell dumpsys window w |grep \/ |grep name=

adb shell "dumpsys window w|grep \/|grep name=|sed 's/mSurface=Surface(name=//g'|sed 's/)//g'|sed 's/ //g'"

adb shell pm clear com.baidu.searchbox   包名  清理包的缓存数据  
"""


class App:
    driver :WebDriver =None

    @classmethod
    def app(cls):
        desired_caps = {}
        desired_caps["automationName"] = "UiAutomator2"
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['appPackage'] = 'com.tencent.mm'
        # desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['appPackage'] = 'com.kook.im'
        desired_caps['appActivity'] = 'com.kook.im.ui.welcome.SplashActivity'
        # appium提供的一种输入法，可以传中文。测试时直接用这个输入法
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"  # 程序结束时重置原来的输入法
        desired_caps["noReset"] = "True"  # 不初始化手机app信息（类似不清楚缓存）
        desired_caps['automationName'] = 'appium'
        desired_caps['deviceName'] = '8KE5T19724017480'
        desired_caps['platformVersion'] = '10'
        desired_caps['autoGrantPermissions'] = 'True' # 这个是appium启动的时候处理各种权限弹窗  赋予全部权限
        # udid = os.getenv("UDID", None)
        # if udid != None:
        #     desired_caps["udid"] = udid
        #     print("udid={}".format(udid))
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # cls.driver = webdriver.Remote("http://192.168.100.165:4444/wd/hub", desired_caps)  # grid 的地址
        cls.driver.implicitly_wait(10)

        for i in range(3): # app 启动的时候会有一些全县的弹窗 这块可以把它给去掉 autoGrantPermissions 这个有的时候不管用
            loc = ("xpath", "//*[@text='始终允许']")
            try:
                e = WebDriverWait(cls.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass
        # 账号，密码，登陆
        cls.driver.find_element_by_id(
            "com.kook.im:id/et_accout").send_keys("liuchengxu")
        cls.driver.find_element_by_id(
            "com.kook.im:id/et_password").send_keys("liu65257504")
        cls.driver.find_element_by_id(
            "com.kook.im:id/et_ip").send_keys("27.115.124.242:8282")

        cls.driver.find_element_by_id("com.kook.im:id/btn_login").click()
        return Work_Kanban(cls.driver)   # 启动app之后页面进入 鲶鱼工作台页面


    @classmethod
    def quit(cls):
        cls.driver.quit()