# -*- coding:utf-8 -*-

from home_list_page_ui import HomeListPageUI


class HomeListPage(HomeListPageUI):
    """
    页面对象(PO): HOME列表页面
    """
    def gesture_item(self):
        """
        点击"Gesture"列表项
        """
        self.gesture_item_loc().click()

    def alert_item(self):
        """
        点击"Alert"列表项
        """
        self.alert_item_loc().click()

    def drag_gesture_up(self):
        """
        拖拽一个元素或者在多个坐标之间移动（屏幕上拉）
        """
        self.driver.touch('drag', {'fromX': 200, 'fromY': 400,
                                   'toX': 200, 'toY': 100,
                                   'duration': 2})

    def drag_gesture_down(self):
        """
        拖拽一个元素或者在多个坐标之间移动（屏幕下拉）
        """
        self.driver.touch('drag', {'fromX': 100, 'fromY': 100,
                                   'toX': 100, 'toY': 400,
                                   'duration': 2})
