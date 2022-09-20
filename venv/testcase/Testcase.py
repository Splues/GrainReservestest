from selenium import webdriver
from selenium.webdriver import ActionChains
from PageObject import Testelement
import Calculator
import time
import unittest

#测试用例
class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("测试开始")

        #测试类实例化

    def tearDown(self):
        print("测试结束")

    @classmethod
    def setUpClass(cls):
        """测试准备，传入浏览器驱动"""
        cls.driver = webdriver.Chrome()


    def test_case_1(self):
        """百度搜索测试"""
        page = Testelement.baidu_page(self.driver)
        page.open()
        page.serch("测试")
        print(page.get_title())
        self.assertEqual(page.by_xpath("//input[@value = '测试']"),"测试")

    def test_case_2(self):
        """百度搜索邮箱"""
        page = Testelement.baidu_page(self.driver)
        page.open()
        page.serch("邮箱")
        self.assertEqual(page.get_title(), "邮箱_百度搜索")

    def test_case_3(self):
        """测试基础base层"""
        self.driver.implicitly_wait(10)
        page = Testelement.baidu_page(self.driver)
        page.open()
        page.by_class("s_ipt")
        page.by_name("wd")
