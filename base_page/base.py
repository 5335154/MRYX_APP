import time
from selenium.webdriver.common.by import By

from driver.android_driver import app_driver

#选择地址
def adress():
    driver = app_driver()
    driver.find_element(By.ID, 'cn.missfresh.application:id/iv_address_icon').click()
    driver.find_element(By.ID, 'cn.missfresh.application:id/tv_select_support_city').click()
    driver.find_element(By.ID, 'cn.missfresh.application:id/et_search_address_input').send_keys("成都市")
    driver.find_element(By.ID, 'cn.missfresh.application:id/tvCity').click()
    driver.find_element(By.ID, 'cn.missfresh.application:id/iv_title_bar_left_icon').click()
    time.sleep(2)
    return driver

# 向左滑
def left_swipe(self):
    size = self.driver.get_window_size()
    print(size)
    self.driver.swipe(size['width'] * 0.8, 100, size['width'] * 0.2, 100)


# 向右滑
def right_swipe(self):
    size = self.driver.get_window_size()
    print(size)
    self.driver.swipe(size['width'] * 0.2, 100, size['width'] * 0.8, 100)

