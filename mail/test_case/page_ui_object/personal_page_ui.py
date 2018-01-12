# -*- coding:utf-8 -*-

from base import Base


class PersonalPageUI(Base):
    """
    页面UI对象(PUO): 个人页面UI
    """
    def personal_button_loc(self):
        """
        定位到"PERSONAL"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'PERSONAL',
            'android_by': 'wait_name',
            'android_value': 'PERSONAL',
        })

    def logout_button_loc(self):
        """
        定位到"Logout"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'Logout',
            'android_by': 'wait_name',
            'android_value': 'Logout',
        })
