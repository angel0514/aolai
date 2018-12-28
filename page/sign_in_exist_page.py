from base.base_action import BaseAction
import page


class SignInExistPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_exist_account(self):
        self.click_element(page.sign_in_exist_account_id)
