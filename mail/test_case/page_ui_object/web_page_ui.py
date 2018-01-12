# -*- coding:utf-8 -*-

from base import Base


class WebPageUI(Base):
    """
    页面UI对象(PUO): Web页面UI
    """
    def baidu_button_loc(self):
        """
        定位到"Baidu"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'Baidu',
            'android_by': 'wait_name',
            'android_value': 'Baidu',
        })

    def search_input_loc(self):
        """
        定位到搜索输入框
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'id',
            'ios_value': 'index-kw',
            'android_by': 'wait_id',
            'android_value': 'index-kw',
        })

    def search_button_loc(self):
        """
        定位到搜索按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'id',
            'ios_value': 'index-bn',
            'android_by': 'wait_id',
            'android_value': 'index-bn',
        })
