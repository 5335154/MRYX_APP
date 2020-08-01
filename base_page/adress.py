import time
from selenium.webdriver.common.by import By


def adress(driver):  #选择地址
    driver.find_element(By.ID, 'cn.missfresh.application:id/iv_address_icon').click()
    driver.find_element(By.ID, 'cn.missfresh.application:id/tv_select_support_city').click()
    driver.find_element(By.ID, 'cn.missfresh.application:id/et_search_address_input').send_keys("成都市")
    driver.find_element(By.ID, 'cn.missfresh.application:id/tvCity').click()
    driver.find_element(By.ID, 'cn.missfresh.application:id/iv_title_bar_left_icon').click()
    time.sleep(2)

