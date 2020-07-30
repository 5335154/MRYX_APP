import unittest

from base_page.adress import adress
from page.shopping_cart_page import Shopping_CartPage


class Shopping_CartTestCase(unittest.TestCase):
    '''购物车内增删改查'''
    def setUp(self):
        self.driver = adress()

    def tearDown(self):
        self.driver.quit()

    def test_shopping_cart(self):
        sc = Shopping_CartPage(self.driver)
        result = sc.shopping_cart()
        self.assertEqual("true", result)


if __name__ == '__main__':
    unittest.main()
