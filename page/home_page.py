
import page
from base.base_action import BaseAction


class HomePage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_me_btn(self):
        self.click_element(page.home_my_button)
