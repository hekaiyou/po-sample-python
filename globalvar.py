# -*- coding:utf-8 -*-


# 项目绝对路径
global_path = '/Users/hekaiyou/PycharmProjects/po-sample-python/'

# 服务器URL
server_url = 'http://localhost:3456/wd/hub'

# 配置iOS的参数
ios_capabilities = {
    'platformName': 'ios',
    'deviceName': 'iPhone 6s',
    'app': 'ios-app-bootstrap.app',
}

# 配置Android的参数
android_capabilities = {
    'platformName': 'android',
    'app': 'android_app_bootstrap-debug.apk',
}

# 测试平台（android/ios）
platform = 'android'
