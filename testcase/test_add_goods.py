import unittest

from base_page.huwei_adress import hw_adress
from driver.huwei_driver import hw_driver
from page.add_goods_detail_page import AddGoods


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = hw_driver()  # 实例化浏览器
        hw_adress(self.driver)  # 填写地址
        self.ag = AddGoods(self.driver)  # 实例化添加商品类

    def tearDown(self):
        self.driver.quit()  # 退出浏览器

    def test_add_good_details(self):
        '''详情页面加入购物车并查看'''
        self.ag.add_good_details()

    def test_buy_good_now(self):
        '''商品详情页面立即购买'''
        self.ag.buy_good_now()


if __name__ == '__main__':
    unittest.main()
