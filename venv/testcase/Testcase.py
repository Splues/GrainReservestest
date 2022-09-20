from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from PageObject import Testelement
import Calculator
import time
import unittest



#设置10s隐式等待
#driver.implicitly_wait(10)

#测试用例
class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def baidu(self,key):
        """登录封装"""
        driver.get(key)

    def test_case_1(self):
        """百度搜索测试"""
        self.baidu("https://www.baidu.com/")
        driver.find_element(By.ID, "kw").send_keys("测试")
        driver.find_element(By.ID, "su").send_keys(Keys.ENTER)

    def test_case_2(self):
        """百度搜索邮箱"""
        driver.get("https://www.baidu.com/")
        driver.find_element(By.ID, "kw").clear()
        driver.find_element(By.ID, "kw").send_keys("163邮箱")
        driver.find_element(By.ID, "su").send_keys(Keys.ENTER)

    def test_case_3(self):
        """测试基础base层"""
        self.driver.implicitly_wait(10)
        page = Testelement.baidu_page(self.driver)
        page.open()
        page.by_class("s_ipt")
        page.by_name("wd")
