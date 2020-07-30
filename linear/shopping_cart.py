'''购物车内增删改查'''
import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    'platformName':'Android',
    'deviceName':'127.0.0.1:92001',
    'platformVersion':'5.1.1',
    'appPackage':'cn.missfresh.application',
    'appActivity':'cn.missfresh.module.base.main.view.SplashActivity',
    'newCommandTimeout':600
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
driver.implicitly_wait(30)

#用户隐私保护提示，点击同意
driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="cn.missfresh.application:id/tv_double_btn_ok"]').click()

#选择地址
driver.find_element(By.ID,'cn.missfresh.application:id/iv_address_icon').click()
driver.find_element(By.ID,'cn.missfresh.application:id/tv_select_support_city').click()
driver.find_element(By.ID,'cn.missfresh.application:id/et_search_address_input').send_keys("成都市")
driver.find_element(By.ID,'cn.missfresh.application:id/tvCity').click()
driver.find_element(By.ID,'cn.missfresh.application:id/iv_title_bar_left_icon').click()
time.sleep(2)

#点击购物车
driver.find_element(By.ID,'cn.missfresh.application:id/cartTab').click()
#添加两件商品
driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/'
                             'android.widget.ImageView[2]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/'
                             'android.widget.ImageView[2]').click()
#增加数量5个
for i in range(5):
    driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/'
                                 'android.widget.ImageView[4]').click()
#减少数量3个
for m in range(3):
    driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/'
                                 'android.widget.ImageView[3]').click()
#查看详情
driver.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.missfresh.application:id/rcv_product"]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]').click()
#返回
driver.find_element(By.ID,'cn.missfresh.application:id/img_back').click()
#取消一个选中
driver.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.missfresh.application:id/rcv_product"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]').click()
#删除
driver.find_element(By.ID,'cn.missfresh.application:id/tv_delete').click()
#取消
driver.find_element(By.ID,'cn.missfresh.application:id/tv_search').click()
#全选
driver.find_element(By.XPATH,'//android.widget.LinearLayout[@resource-id="cn.missfresh.application:id/sticky"]/android.widget.ImageView[1]').click()
#删除
driver.find_element(By.ID,'cn.missfresh.application:id/tv_delete').click()
#确定
driver.find_element(By.ID,'cn.missfresh.application:id/tv_ensure').click()

driver.quit()