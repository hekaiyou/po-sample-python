# -*- coding:utf-8 -*-

from webview_page_ui import WebviewPageUI


class WebviewPage(WebviewPageUI):
    """
    页面对象(PO): Webview页面
    """
    def webview_button(self):
        """
        点击"Webview"按钮
        """
        self.webview_button_loc().click()

    def pushview_button(self):
        """
        点击"pushView"按钮
        """
        self.pushview_button_loc().click()

    def popview_button(self):
        """
        点击"popView"按钮
        """
        self.popview_button_loc().click()
