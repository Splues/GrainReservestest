##################################
#版本0.2
#完成功能：基础元素定位以及断言，输出测试报告
#BY:ssy
#2022.9.18
##################################
from testcase import Testcase
import unittest
from HTMLTestRunner import HTMLTestRunner



if __name__ == '__main__':
    #创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(Testcase.TestCalculator("test_case_1"))
    #suit.addTest(Testcase.TestCalculator("test_case_2"))
    #suit.addTest(Testcase.TestCalculator("test_case_3"))



    #模式选择
    modul = 1

    #创建测试运行器
    if modul == 1:
        # 存储html测试报告
        f = open('./result.html', 'w', encoding='utf-8')
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='百度搜索测试报告', description='用例执行情况：')
    elif modul == 2:
        runner = unittest.TextTestRunner()
    else :
        runner = unittest.TextTestRunner()

    #参数1：存储报告地址；参数2：标题；参数3：小标题；
    runner.run(suit)

    if modul == 1:
        f.close()
    else:
        print("未输出测试报告")



