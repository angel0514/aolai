from base.base_action import BaseAction
import page,time


class LoginInPage(BaseAction):

    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    def login_in(self,name,pwd):
        time.sleep(1)
        #输入账号
        self.input_element_content(page.login_username_id,name)

        #输入密码
        self.input_element_content(page.login_password_id, pwd)
        #点击登录
        self.click_element(page.login_login_in_btn)

    def log_out(self):
        self.click_element(page.login_login_out_btn)
