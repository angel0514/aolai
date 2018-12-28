import os
import sys
sys.path.append(os.getcwd())
import pytest
from base.base_driver import init_driver
from base.read_yaml_data import read_data
from page.navigation_page import NavigationPage


def get_data():
    data_list = []
    data = read_data("login_data.yaml")
    for i in data.keys():
        data2 = data.get(i)
        name = data2.get("username")  # name = data2["username"]若不存在这个键会报错,若是用get则返回NONE,不会报错
        password = data2.get("password")
        tag = data2.get("tag")
        toast_msg = data2.get("toast_msg")
        expect_msg = data2.get("expect_msg")
        data_list.append((name, password, tag, toast_msg, expect_msg))
    return data_list


class TestLogin:

    def setup_class(self):
        self.driver = init_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navigation_page = NavigationPage(self.driver)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('username,password,tag,toast_msg,expect_msg', get_data())
    def test_login(self, username, password, tag, toast_msg, expect_msg):
        self.navigation_page.get_home_page_obj().click_me_btn()
        self.navigation_page.get_sign_in_page_obj().click_exist_account()
        self.navigation_page.get_login_page_obj().login_in(username, password)
        if tag == 1:
            try:
                login_state = self.navigation_page.get_person_center_page_obj().is_login_success()
                self.navigation_page.get_person_center_page_obj().click_person_center_setting()
                self.navigation_page.get_person_center_page_obj().swipe_screen(1)
                self.navigation_page.get_setting_page_obj().logout_account()
                assert login_state, self.navigation_page.get_person_center_page_obj().get_screen()
            except:
                # 截图 在哪一个页面出现的问题
                self.navigation_page.get_person_center_page_obj().get_screen()
                self.navigation_page.get_login_page_obj().log_out()
        else:
            try:
                get_toast_message = self.navigation_page.get_person_center_page_obj().get_toast_message(toast_msg)
                assert get_toast_message == expect_msg, self.navigation_page.get_person_center_page_obj().get_screen()
            finally:
                # 5.关闭当前登录页面
                self.navigation_page.get_login_page_obj().log_out()
