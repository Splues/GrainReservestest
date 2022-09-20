#PO封装，用于存储测试用例的元素
from selenium.webdriver.common.by import By

class Base():
    """基础page层,通用方法"""
    def __init__(self,driver):
        self.driver = driver

    #打开页面
    def open(self,url = None):
        if url is None:
            self.driver.get(self.url)
        else :
            self.driver.get(url)

    #定位方法封装
    def by_id(self,id):
        return self.driver.find_element(By.ID, id)

    def by_name(self,name):
        return self.driver.find_element(By.NAME, name)

    def by_class(self,class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def by_tag(self,tag):
        return self.driver.find_element(By.TAG_NAME, tag)

    def by_text(self,text):
        return self.driver.find_element(By.LINK_TEXT, text)

    def by_ptext(self,ptext):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, ptext)

    def by_xpath(self,xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def by_css(self,css):
        return self.driver.find_element(By.CSS_SELECTOR, css)

class baidu_page(Base):
    """业务通用方法"""
    url = "https://www.baidu.com/"



