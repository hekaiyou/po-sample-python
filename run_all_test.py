# -*- coding:utf-8 -*-

import unittest
import time
from HTMLTestRunnerCN import HTMLTestRunner
from globalvar import global_path


# 指定测试用例为当前文件夹下的test_case目录
test_dir = './mail/test_case'
# 自动根据测试目录匹配查找测试用例文件，并将查找到的测试用例组装到测试套件
discover = unittest.defaultTestLoader.discover(test_dir, pattern = '*_case.py')


if __name__ == "__main__":
    # 获取时间并转换为特定格式
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 组成测试报告的绝对路径
    filename = global_path + '/mail/report/'+now+'报告.html'
    # 打开一个文件，写入测试报告
    fp = open(filename, 'wb')
    # 生成测试报告
    runner = HTMLTestRunner(stream=fp, title='自动化测试报告', description='测试用例描述', tester='测试人员')
    # 执行找到的测试套件
    runner.run(discover)
    # 关闭文件
    fp.close()
