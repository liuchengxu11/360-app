from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time


class Config_page:

    _black_list = [
        (By.XPATH,
         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView[2]"),
    ]  # 这个就是写的在执行过程中出现的各种弹窗，广告

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except BaseException:
            self.handle_exception()
            # self.find_element(locator)
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):  # 有时候单纯的点击也会有异常封装一个点击的方法
        print("点击一个元素   ——{}".format(locator))
        try:
            # 如果click也有异常，可以这样处理
            self.find_element(locator).click()
            print("--------成功----------")
        except BaseException:
            self.handle_exception()
            self.find_element(locator).click()

    def find_element_and_sendkeys(self, locator, sendkeys="", dian=None):  # 封装一个输入的方法
        print("sendkkeys={}".format(sendkeys))
        if dian is not None:
            try:
                self.find_element(locator).click()
                self.find_element(locator).clear()
                self.find_element(locator).send_keys(sendkeys)
                self.find_element(dian).click()

            except BaseException:
                self.handle_exception()
                self.find_element(locator).click()
                self.find_element(locator).clear()
                self.find_element(locator).send_keys(sendkeys)
                self.find_element(dian).click()
        else:
            try:
                self.find_element(locator).click()
                self.find_element(locator).clear()
                self.find_element(locator).send_keys(sendkeys)

            except BaseException:
                self.handle_exception()
                self.find_element(locator).click()
                self.find_element(locator).clear()
                self.find_element(locator).send_keys(sendkeys)

    def handle_exception(self):
        print(":exception")
        self.driver.implicitly_wait(0)  # 这里先设置隐式等待为0秒加快异常的处理速度然后在结束的时候设置回来
        for locator in self._black_list:
            print(locator)
            elements = self.driver.find_elements(*locator)

            if len(elements) >= 1:
                # 通过循环看自己弹窗的元素id是否找到  找到后就点击
                elements[0].click()
            else:
                print("%s not found" % str(locator))

        self.driver.implicitly_wait(10)



