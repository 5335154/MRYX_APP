import unittest

from driver.android_driver import app_driver
from page.my_page import MyPage


class LoginTestCase(unittest.TestCase):
    '''微信登录'''
    def setUp(self):
        self.driver = app_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        lg = MyPage(self.driver)
        result = lg.login()

        self.assertEqual("退出登录", result)


if __name__ == '__main__':
    unittest.main()
