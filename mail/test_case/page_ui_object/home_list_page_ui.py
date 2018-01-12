# -*- coding:utf-8 -*-

from base import Base


class HomeListPageUI(Base):
    """
    页面UI对象(PUO): HOME列表页面UI
    """
    def gesture_item_loc(self):
        """
        定位到"Gesture"列表项
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'Gesture',
            'android_by': 'wait_name',
            'android_value': 'Gesture',
        })

    def alert_item_loc(self):
        """
        定位到"Alert"列表项
        :return: WebDriver对象
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'Alert',
            'android_by': 'wait_name',
            'android_value': 'Alert',
        })
