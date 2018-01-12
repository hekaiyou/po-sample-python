# -*- coding:utf-8 -*-

import unittest
from retrying import retry
from driver import drivers


class AppTest(unittest.TestCase):
    """
    测试类，父类为unittest.TestCase
    继承unittest.TestCase的方法与各种断言
    """
    @classmethod
    def setUpClass(cls):
        """
        在所有测试用例运行前运行一次
        """
        cls.driver = drivers()
        cls.initDriver()

    @classmethod
    def tearDownClass(cls):
        """
        在所有测试用例运行完后运行一次
        """
        cls.driver.quit()

    @classmethod
    @retry
    def initDriver(cls):
        """
        在运行测试用例前初始化
        """
        print("正在连接服务器...")
        # 初始化WebDriver服务器
        cls.driver.init()
