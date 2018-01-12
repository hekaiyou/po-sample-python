# -*- coding:utf-8 -*-

from macaca import WebDriver
import globalvar


def drivers():
    """
    根据全局平台参数返回对应的驱动
    :return: WebDriver对象
    """
    desired_caps = {}
    if globalvar.platform == 'ios':
        # 把iOS字典的键/值对更新到desired_caps里
        desired_caps.update(globalvar.ios_capabilities)
    elif globalvar.platform == 'android':
        # 把Android字典的键/值对更新到desired_caps里
        desired_caps.update(globalvar.android_capabilities)
    else:
        pass
    # 修改字典中已有键/值对
    desired_caps['app'] = globalvar.global_path + 'driver/' + desired_caps['app']
    # 配置所需的功能和服务器URL的WebDriver对象
    driver = WebDriver(desired_caps, globalvar.server_url)
    return driver
