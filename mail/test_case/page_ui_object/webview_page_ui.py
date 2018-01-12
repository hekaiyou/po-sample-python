# -*- coding:utf-8 -*-

from base import Base


class WebviewPageUI(Base):
    """
    页面UI对象(PUO): Webview页面UI
    """
    def webview_button_loc(self):
        """
        定位到"Webview"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'Webview',
            'android_by': 'wait_name',
            'android_value': 'Webview',
        })

    def pushview_button_loc(self):
        """
        定位到"pushView"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'id',
            'ios_value': 'pushView',
            'android_by': 'wait_id',
            'android_value': 'pushView',
        })

    def popview_button_loc(self):
        """
        定位到"popView"按钮
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'id',
            'ios_value': 'popView',
            'android_by': 'wait_id',
            'android_value': 'popView',
        })
