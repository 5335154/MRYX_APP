import unittest

from driver.android_driver import app_driver
from page.home_page import HomePage


class Flow_BuyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = app_driver()

    def tearDown(self):
        self.driver.quit()

    def test_flow_buy(self):
        home = HomePage(self.driver)
        home.adress("成都市", "东方广场C座")
        result = home.flow_buy()

        self.assertEqual("设备存在风险，请更换设备下单", result)


if __name__ == '__main__':
    unittest.main()
