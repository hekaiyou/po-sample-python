# -*- coding:utf-8 -*-

from home_page_ui import HomePageUI


class HomePage(HomePageUI):
    """
    页面对象(PO): HOME页面
    """
    def home_button(self):
        """
        点击"HOME"按钮
        """
        self.home_button_loc().click()

    def list_button(self):
        """
        点击"list"按钮
        """
        self.list_button_loc().click()
