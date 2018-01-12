# -*- coding:utf-8 -*-

from base import Base


class HomePageUI(Base):
    """
    页面UI对象(PUO): HOME页面UI
    """
    def home_button_loc(self):
        """
        定位到"HOME"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'HOME',
            'android_by': 'wait_name',
            'android_value': 'HOME',
        })

    def list_button_loc(self):
        """
        定位到"list"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'list',
            'android_by': 'wait_name',
            'android_value': 'list',
        })
