# -*- coding:utf-8 -*-

from globalvar import global_path


def insert_img(driver, file_name):
    """
    截图并保存到图片目录
    :param driver: WebDriver对象
    :param file_name: 截图文件名
    """
    # 将多个路径组合成截图存放路径
    file_path = global_path + '/mail/report/image/' + file_name + '.png'
    # 将截图保存到本地
    driver.save_screenshot(file_path)


def switch_to_webview(driver):
    """
    切换到WebView模式
    :param driver: WebDriver对象
    :return: WebDriver对象
    """
    # 获取可用的上下文列表
    contexts = driver.contexts
    # 切换到WebView
    driver.context = contexts[-1]
    # 返回WebDriver对象
    return driver


def switch_to_native(driver):
    """
    切换到Native模式
    :param driver: WebDriver对象
    :return: WebDriver对象
    """
    # 获取可用的上下文列表
    contexts = driver.contexts
    # 切换到Native
    driver.context = contexts[0]
    # 返回WebDriver对象
    return driver
