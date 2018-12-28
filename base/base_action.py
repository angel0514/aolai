import time

from selenium.webdriver.common.by import By


class BaseAction:
    # 当类初始化的时候这个方法就执行
    def __init__(self, driver):
        self.driver = driver

    # 把一些常见的操作定义出来 (点击 输入内容)
    def click_element(self, loc):

        # 到底点击哪个元素 是不是的先找到这个元素才能点击
        self.find_element(loc).click()

    def input_element_content(self, loc, content):
        time.sleep(1)
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(content)

    """
      loc代表要传递一个元祖进来 返回找到的元素
    """

    def find_element(self, loc):
        time.sleep(1)
        # 在找元素之前 等待
        # self.driver.implicitly_wait(5)
        return self.driver.find_element(loc[0], loc[1])

    def swipe_screen(self, tag):
        time.sleep(1)
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        if tag == 1:  # 向下滑动
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:  # 向上滑动
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:  # 向左滑动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:  # 向右滑动
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

    # 获取吐司的消息
    def get_toast_message(self, message):
        toast_xpath = "//*[contains(@text,'{}')]".format(message)
        toast_message = self.find_element((By.XPATH, toast_xpath)).text
        return toast_message

    # .截图
    def get_screen(self):
        # 截图名称
        png_name = "./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)

        # with open("abc.png", "rb") as f:
        # allure.attach("截图名字", f.read(), allure.attach_type.PNG)
