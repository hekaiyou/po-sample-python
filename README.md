# 使用PageObject+跨平台改造Macaca示例

在学习完Macaca基础后，就迫不及待的模仿着Macaca示例项目，开始了测试用例的开发，并且在几天时间里就完成了几个页面的测试。然而，此时项目的所有代码都放在一个.py文件里，该文件已有上千行代码，重复代码很多，维护起来很困难。更大的问题是，我需要给Android和iOS分别写一套代码，这个工作量太多，而且大多是重复代码。

![Macaca网络图片](http://upload-images.jianshu.io/upload_images/6218810-8198df64b621fe8e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

为了避免这种情况发生，可以使用PageObject设计模式开发Macaca项目，封装页面对象与用例分离，再把页面对象中定位UI元素的部分脱离，封装成页面UI对象。

## 项目目录结构

首先，先建立一个下图所示的项目目录结构：

![项目目录结构](http://upload-images.jianshu.io/upload_images/6218810-81eb83259103ee1d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如上图，根目录下面有driver和mail两个文件夹，其中driver是用于存放驱动，mail用于存放项目的测试用例、测试报告以及测试数据等，同目录下还有run_all_test.py文件，用于运行项目的所有自动化用例。

在mail文件夹下，有data、report、test_case三个文件夹，其中data用于存放测试数据，report用于存放测试报告，test_case用于存放测试用例。在test_case文件夹下，有model和page_object两个文件夹，其中model用于存放配置函数及公共类，page_object用于存放页面对象，同目录下还有macaca_case.py这个测试用例文件。

在report文件夹下，有image和template两个文件夹，其中image用于存放测试过程中的截图，template用于存放生成测试报告的工具，例如HTMLTestRunner。

## 全局配置文件

在项目根目录下新建[globalvar.py](https://github.com/hekaiyou/po-sample-python/blob/master/globalvar.py)文件，编写全局配置文件：

```
global_path = '/Users/hekaiyou/PycharmProjects/po-sample-python/'

server_url = 'http://localhost:3456/wd/hub'

ios_capabilities = {
    'platformName': 'ios',
    'deviceName': 'iPhone 6s',
    'app': 'ios-app-bootstrap.app',
}

android_capabilities = {
    'platformName': 'android',
    'app': 'android_app_bootstrap-debug.apk',
}

platform = 'android'
```

在全局配置文件中设置项目的绝对路径、Android与iOS平台的驱动参数、当前测试平台的名称。以后只要更改当前测试平台的名称，即platform参数，就可以选择当前要测试的是Android还是iOS设备。

## 编写公共模块

在.../mail/test_case/model文件夹下新建[driver.py](https://github.com/hekaiyou/po-sample-python/blob/master/mail/test_case/model/driver.py)文件，编写公共驱动文件，它可以根据platform参数去调用对应平台的驱动：

```
from macaca import WebDriver
import globalvar

def drivers():
    desired_caps = {}
    if globalvar.platform == 'ios':
        desired_caps.update(globalvar.ios_capabilities)
    elif globalvar.platform == 'android':
        desired_caps.update(globalvar.android_capabilities)
    else:
        pass

    desired_caps['app'] = globalvar.global_path + 'driver/' + desired_caps['app']
    driver = WebDriver(desired_caps, globalvar.server_url)
    return driver
```

在.../mail/test_case/model文件夹下新建[function.py](https://github.com/hekaiyou/po-sample-python/blob/master/mail/test_case/model/function.py)文件，编写公共函数文件，它简单的实现截图函数、切换WebView函数、切换Native函数：

```
from globalvar import global_path

def insert_img(driver, file_name):
    file_path = global_path + '/mail/report/image/' + file_name + '.png'
    driver.save_screenshot(file_path)

def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver
```

在.../mail/test_case/model文件夹下新建[appunit.py](https://github.com/hekaiyou/po-sample-python/blob/master/mail/test_case/model/appunit.py)文件，编写公共测试类文件，它会调用公共驱动文件来初始化WebDriver服务器：

```
import unittest
from retrying import retry
from driver import drivers

class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = drivers()
        cls.initDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    @retry
    def initDriver(cls):
        print("正在连接服务器...")
        cls.driver.init()
```

在.../mail/test_case/model文件夹下新建[base.py](https://github.com/hekaiyou/po-sample-python/blob/master/mail/test_case/model/base.py)文件，编写基础类文件，它接收页面UI对象中的定位字典，再根据字典内容返回查找到的元素：

```
from globalvar import platform

class Base(object):
    def __init__(self, driver):
        self.driver = driver
        self.platform = platform

    def selector(self, location):
        by = None
        value = None
        if 'by' in location:
            by = location['by']
            value = location['value']
        ······
        else:
            pass
        if by == 'xpath':
            return self.xpath(value)
       ······
        else:
            pass

    def xpath(self, xpath):
        return self.driver.element_by_xpath(xpath)

   ······
```

## 编写页面UI对象

在.../mail/test_case/page_ui_object文件夹下新建[home_page_ui.py](https://github.com/hekaiyou/po-sample-python/blob/master/mail/test_case/page_ui_object/home_page_ui.py)文件，编写HOME页面UI对象类文件，它将定位字典传给基础类以获取对应的元素对象：

```
from base import Base

class HomePageUI(Base):
    def home_button_loc(self):
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'HOME',
            'android_by': 'wait_name',
            'android_value': 'HOME',
        })
    ······
```

定位字典的结构有两种，当iOS与Android的UI元素的定位方法与参数各不相同时：

```
{
    'ios_by': 'ios_by',
    'ios_value': 'ios_value',
    'android_by': 'android_by',
    'android_value': 'android_value',
}
```

当iOS与Android的UI元素的定位方法与参数相同时：

```
{
    'by': 'by',
    'value': 'value',
}
```

所有页面UI对象类文件的结构都和上面一样。

## 编写页面对象

在.../mail/test_case/page_object文件夹下新建[home_page.py](https://github.com/hekaiyou/po-sample-python/blob/master/mail/test_case/page_object/home_page.py)文件，编写HOME页面对象类文件，它调用对应的页面UI对象类，实现当前页面的所有相关操作：

```
from home_page_ui import HomePageUI

class HomePage(HomePageUI):
    def home_button(self):
        self.home_button_loc().click()

    def list_button(self):
        self.list_button_loc().click()
```

这样的页面对象类非常简洁，代码清晰明了，所有页面对象类文件的结构都和上面一样。

## 编写测试用例

在.../mail/test_case文件夹下新建[macaca_case.py](https://github.com/hekaiyou/po-sample-python/blob/master/mail/test_case/macaca_case.py)文件，编写测试用例类文件：

```
import appunit
from time import sleep
from login_page import LoginPage

class MacacaTest(appunit.AppTest):
    def test_01_login(self):
        login_po = LoginPage(self.driver)
        login_po.username_input('中文+Test+12345678')
        login_po.password_input('111111')
        sleep(2)
        login_po.login_button()
    ······
```

## 执行测试用例

在项目根目录下新建[run_all_test.py](https://github.com/hekaiyou/po-sample-python/blob/master/run_all_test.py)文件，编写用例执行代码文件：

```
import unittest
import time
from HTMLTestRunnerCN import HTMLTestRunner
from globalvar import global_path

test_dir = './mail/test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern = '*_case.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = global_path + '/mail/report/'+now+'报告.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='自动化测试报告', description='测试用例描述', tester='测试人员')
    runner.run(discover)
    fp.close()
```

这样我们就实现了一个用例对象、页面对象、页面UI对象分离的开发模式，没有重复代码，又易于维护，美滋滋...

> 为什么选择？有的人喜欢创造世界，他们做了程序员。有的人喜欢拯救世界，他们做了测试员。
