from selenium.webdriver.common.by import By


def hw_adress(driver):
    #点击确定
    driver.find_element(By.ID,'cn.missfresh.application:id/tv_double_btn_ok').click()

    #点击定位
    driver.find_element(By.ID, 'cn.missfresh.application:id/address_tv').click()
    #点击输入框
    driver.find_element(By.ID, 'cn.missfresh.application:id/et_search_input').click()
    #输入东方广场
    driver.find_element(By.ID, 'cn.missfresh.application:id/et_search_input').send_keys('成都市东方广场')
    #选择东方广场
    driver.find_element(By.XPATH, '//*[@text="东方广场"]').click()
