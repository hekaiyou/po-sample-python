# -*- coding:utf-8 -*-

from base import Base


class LoginPageUI(Base):
    """
    页面UI对象(PUO): 登录页面UI
    """
    def username_input_loc(self):
        """
        定位到登录用户名输入框
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeTextField[1]',
            'android_by': 'class_name',
            'android_value': ['android.widget.EditText', 0],
        })

    def password_input_loc(self):
        """
        定位到登录密码输入框
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//XCUIElementTypeSecureTextField[1]',
            'android_by': 'class_name',
            'android_value': ['android.widget.EditText', 1],
        })

    def login_button_loc(self):
        """
        定位到登录按钮
        :return: WebDriver对象
        """
        return self.selector({
            'by': 'name',
            'value': 'Login',
        })
