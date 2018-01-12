# -*- coding:utf-8 -*-

from base import Base


class HomeListGesturePage(Base):
    """
    页面对象(PO): HOME列表手势页面
    """
    def tap_gesture(self):
        """
        点击某个坐标或者当前元素
        """
        self.driver.touch('tap', {'x': 100, 'y': 100})

    def press_gesture(self):
        """
        长按某个坐标或者当前元素（duration）
        """
        self.driver.touch('press', {'x': 100, 'y': 100,
                                    'duration': 1})

    def press_gesture_steps(self):
        """
        长按某个坐标或者当前元素（steps）
        """
        self.driver.touch('press', {'x': 100, 'y': 100,
                                    'steps': 100})

    def double_tap_gesture(self):
        """
        双击某个坐标或者当前元素
        """
        self.driver.touch('doubleTap', {'x': 100, 'y': 100})

    def drag_gesture(self):
        """
        拖拽一个元素或者在多个坐标之间移动（steps）
        """
        self.driver.touch('drag', {'fromX': 100, 'fromY': 100,
                                   'toX': 100, 'toY': 600,
                                   'steps': 100})
