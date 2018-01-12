# -*- coding:utf-8 -*-

from web_page_ui import WebPageUI


class WebPage(WebPageUI):
    """
    页面对象(PO): Web页面
    """
    def baidu_button(self):
        """
        点击"Baidu"按钮
        """
        self.baidu_button_loc().touch('tap')

    def search_input(self, text):
        """
        在搜索框输入文本
        """
        self.search_input_loc().send_keys(text)

    def search_button(self):
        """
        点击搜索按钮
        """
        self.search_button_loc().click()
