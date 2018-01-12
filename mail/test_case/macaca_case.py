# -*- coding:utf-8 -*-

import appunit
from time import sleep
from function import insert_img
from function import switch_to_webview
from function import switch_to_native
from login_page import LoginPage
from home_page import HomePage
from home_list_page import HomeListPage
from home_list_gesture_page import HomeListGesturePage
from webview_page import WebviewPage
from web_page import WebPage
from personal_page import PersonalPage


class MacacaTest(appunit.AppTest):
    """Macaca示例App测试"""
    def test_01_login(self):
        """登录"""
        login_po = LoginPage(self.driver)
        login_po.username_input('中文+Test+12345678')
        login_po.password_input('111111')
        sleep(2)
        login_po.login_button()

    def test_02_scroll_tableview(self):
        """滚动表视图"""
        home_po = HomePage(self.driver)
        home_po.home_button()
        home_po.list_button()

    def test_03_gesture(self):
        """手势"""
        home_list_po = HomeListPage(self.driver)
        sleep(2)
        home_list_po.alert_item()
        sleep(2)
        # 接受可用的警报
        self.driver.accept_alert()
        sleep(2)
        # 返回上一级
        self.driver.back()
        sleep(2)
        home_list_po.drag_gesture_up()
        sleep(2)
        home_list_po.drag_gesture_down()
        sleep(2)
        home_list_po.gesture_item()
        sleep(2)
        home_list_gesture_po = HomeListGesturePage(self.driver)
        home_list_gesture_po.tap_gesture()
        home_list_gesture_po.press_gesture()
        home_list_gesture_po.double_tap_gesture()
        home_list_gesture_po.press_gesture_steps()
        home_list_gesture_po.drag_gesture()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.back()

    def test_04_webview(self):
        """Web视图"""
        webview_po = WebviewPage(self.driver)
        webview_po.webview_button()
        sleep(3)
        insert_img(self.driver, 'webView')
        switch_to_webview(self.driver)
        webview_po.pushview_button()
        sleep(3)
        webview_po.popview_button()

    def test_05_web(self):
        """Baidu.com"""
        switch_to_native(self.driver)
        web_po = WebPage(self.driver)
        web_po.baidu_button()
        sleep(3)
        insert_img(self.driver, 'baidu')
        switch_to_webview(self.driver)
        web_po.search_input('macaca')
        sleep(3)
        web_po.search_button()

    def test_06_logout(self):
        """退出"""
        switch_to_native(self.driver)
        personal_po = PersonalPage(self.driver)
        personal_po.personal_button()
        personal_po.logout_button()
