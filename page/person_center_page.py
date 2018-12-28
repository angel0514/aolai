from base.base_action import BaseAction
import page


class PersonCenterPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 点击个人中心的设置按钮
    def click_person_center_setting(self):
        self.click_element(page.person_center_setting_btn)

    # 判断一下是否登录成功 如果登录成功返回true 登录失败就返回false
    def is_login_success(self):
        try:
            self.find_element(page.person_center_all_order)
            return True
        except:
            return False
