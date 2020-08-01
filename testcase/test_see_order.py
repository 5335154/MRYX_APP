import unittest

from base_page.huwei_adress import hw_adress
from driver.huwei_driver import hw_driver
from page.see_order_page import SeeOrderPage


class TestSeeOrder(unittest.TestCase):
    '''查看我的订单'''
    def setUp(self):
        self.driver = hw_driver()    #实例化浏览器
        hw_adress(self.driver)           #填写地址
        self.catpay = SeeOrderPage(self.driver)  #实例化查看订单类
    def tearDown(self):
        self.driver.quit()    #退出浏览器

    def test_cat_pay(self):
        '''查看待支付订单'''
        self.catpay.cat_pay()

    def test_cat_wait_send(self):
        '''查看待配送'''
        self.catpay.cat_wait_send()

    def test_cat_send(self):
        '''查看配送中'''
        self.catpay.cat_send()

    def test_cat_evaluate(self):
        '''查看待评价'''
        self.catpay.cat_evaluate()

    def test_cat_refund(self):
        '''查看售后'''
        self.catpay.cat_refund()






if __name__ == '__main__':
    unittest.main()
