import time

from selenium.webdriver.common.by import By


class LoginPage():
    '''登录'''
    def __init__(self,driver):
        self.driver = driver

        #定位
        self.loc_click_my = (By.ID, 'cn.missfresh.application:id/mineTab')  # 点击我的
        self.loc_click_login = (By.ID, 'cn.missfresh.application:id/tv_nickname') # 点击登录/注册
        self.loc_click_yes = (By.ID, 'cn.missfresh.application:id/iv_protocol') # 勾选同意协议
        self.loc_wechat_login = (By.ID, 'cn.missfresh.application:id/tv_wx_login')  # 微信登录
        self.loc_click_set = (By.XPATH,'//android.widget.TextView[@text="设置"]')  #设置
        self.loc_click_back = (By.XPATH,'//android.view.View/android.view.View[1]/android.widget.ImageView[1]') #返回
        self.loc_result = (By.XPATH,'//android.widget.Button[@text="退出登录"]') #断言

    def ele_click_my(self): # 点击我的
        self.driver.find_element(*self.loc_click_my).click()

    def ele_click_login(self):    # 点击登录/注册
        self.driver.find_element(*self.loc_click_login).click()

    def ele_click_yes(self):    # 勾选同意协议
        self.driver.find_element(*self.loc_click_yes).click()

    def ele_wechat_login(self):    # 微信登录
        self.driver.find_element(*self.loc_wechat_login).click()

    def ele_set(self):  # 点击设置
        self.driver.find_element(*self.loc_click_set).click()

    def ele_back(self):  #返回
        self.driver.find_element(*self.loc_click_back).click()  #返回登录页面

    def login(self):
        self.ele_click_my()
        self.ele_click_login()
        self.ele_click_yes()
        self.ele_wechat_login()
        self.ele_set()
        time.sleep(1)
        result = self.driver.find_element(*self.loc_result).text
        self.ele_back()
        time.sleep(1)
        return result
