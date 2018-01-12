# -*- coding:utf-8 -*-

from globalvar import platform


class Base(object):
    """
    基本类
    """
    def __init__(self, driver):
        """
        初始化构造器
        :param driver: WebDriver对象
        """
        self.driver = driver
        self.platform = platform

    def selector(self, location):
        """
        根据平台与定位方式的字典查找元素
        :param location: {
            'ios_by': 'ios_by',
            'ios_value': 'ios_value',
            'android_by': 'android_by',
            'android_value': 'android_value',
        }
        :return: WebDriver对象
        """
        by = None
        value = None
        if 'by' in location:
            by = location['by']
            value = location['value']
        elif platform == 'ios':
            by = location['ios_by']
            value = location['ios_value']
        elif platform == 'android':
            by = location['android_by']
            value = location['android_value']
        else:
            pass
        if by == 'xpath':
            return self.xpath(value)
        elif by == 'id':
            return self.id(value)
        elif by == 'wait_id':
            return self.wait_id(value)
        elif by == 'name':
            return self.name(value)
        elif by == 'wait_name':
            return self.wait_name(value)
        elif by == 'class_name':
            return self.class_name(value)
        else:
            pass

    def xpath(self, xpath):
        """
        通过XMLPath查找元素
        :param xpath: 元素的XMLPath
        :return: WebElement对象
        """
        return self.driver.element_by_xpath(xpath)

    def id(self, _id):
        """
        通过ID查找元素
        :param _id: 元素的ID
        :return: WebElement对象
        """
        return self.driver.element_by_id(_id)

    def wait_id(self, _id):
        """
        通过ID查找元素，默认等待10秒，每次间隔1秒
        :param _id: 元素的ID
        :return: WebElement对象
        """
        return self.driver.wait_for_element_by_id(_id)

    def name(self, name):
        """
        通过文本查找元素
        :param name: 元素的文本
        :return: WebElement对象
        """
        return self.driver.element_by_name(name)

    def wait_name(self, name):
        """
        通过文本查找元素，默认等待10秒，每次间隔1秒
        :param name: 元素的文本
        :return: WebElement对象
        """
        return self.driver.wait_for_element_by_name(name)

    def class_name(self, class_name):
        """
        通过[伪类名称,索引]查找元素
        :param class_name: ['class_name', index]
        :return: WebElement对象
        """
        return self.driver.elements_by_class_name(class_name[0])[class_name[1]]
