import unittest

from base_page.huwei_adress import hw_adress
from driver.huwei_driver import hw_driver
from page.page_add_good_page import PageAddGood


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = hw_driver()   # 实例化浏览器
        hw_adress(self.driver)      # 填写地址
        self.pag = PageAddGood(self.driver)  # 实例化页面添加商品类

    def tearDown(self):
        self.driver.quit()  # 退出浏览器

    def test_page_add_good(self):
        '''页面添加商品'''
        self.pag.page_add_good()


if __name__ == '__main__':
    unittest.main()
