# -*- coding:utf-8 -*-

from personal_page_ui import PersonalPageUI


class PersonalPage(PersonalPageUI):
    """
    页面对象(PO): 个人页面
    """
    def personal_button(self):
        """
        点击"PERSONAL"按钮
        """
        self.personal_button_loc().click()

    def logout_button(self):
        """
        点击"Logout"按钮
        """
        self.logout_button_loc().click()
