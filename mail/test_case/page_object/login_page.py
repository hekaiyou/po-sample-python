# -*- coding:utf-8 -*-

from login_page_ui import LoginPageUI


class LoginPage(LoginPageUI):
    """
    页面对象(PO): 登录页面
    """
    def username_input(self, text):
        """
        输入登录用户名
        :param text: 输入文本
        """
        self.username_input_loc().send_keys(text)

    def password_input(self, text):
        """
        输入登录密码
        :param text: 输入文本
        """
        self.password_input_loc().send_keys(text)

    def login_button(self):
        """
        点击登录按钮
        """
        self.login_button_loc().click()
