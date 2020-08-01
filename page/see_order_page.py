from selenium.webdriver.common.by import By

from base_page.adress import adress
from driver.android_driver import app_driver


class SeeOrderPage():
    def __init__(self, driver):
        self.driver = driver
        self.loc_click_mine = (By.ID, 'cn.missfresh.application:id/mineTab')
        self.loc_click_pay = (By.ID, 'cn.missfresh.application:id/btn_mine_pre_pay')
        self.loc_click_wait_send = (By.ID, 'cn.missfresh.application:id/btn_mine_pre_shipping')
        self.loc_click_send = (By.ID, 'cn.missfresh.application:id/btn_mine_shipping')
        self.loc_click_evaluate = (By.ID, 'cn.missfresh.application:id/btn_mine_sign_in')
        self.loc_click_refund = (By.ID, 'cn.missfresh.application:id/btn_mine_after_market')

    def click_mine(self):           #点击我的
        self.driver.find_element(*self.loc_click_mine).click()

    def click_pay(self):            #点击待支付
        self.driver.find_element(*self.loc_click_pay).click()

    def click_wait_send(self):       #点击待配送
        self.driver.find_element(*self.loc_click_wait_send).click()

    def click_send(self):           #点击配送中
        self.driver.find_element(*self.loc_click_send).click()

    def click_evaluate(self):       #点击待评价
        self.driver.find_element(*self.loc_click_evaluate).click()

    def click_refund(self):         #点击售后/退款
        self.driver.find_element(*self.loc_click_refund).click()

    def login_wechat(self):
        try:
            #点击继续使用
            self.driver.find_element(By.ID, 'cn.missfresh.application:id/left_tv').click()

            #点击已阅读协议
            self.driver.find_element(By.ID, 'cn.missfresh.application:id/iv_protocol').click()

            #点击微信
            self.driver.find_element(By.ID, 'cn.missfresh.application:id/tv_wx_login').click()

            #点击继续使用

            self.driver.find_element(By.ID, 'cn.missfresh.application:id/left_tv').click()
        except:
            print('微信登录步骤需要调整')

    def cat_pay(self):
        '''查看待支付'''
        self.click_mine()     #点击我的
        self.click_pay()      #点击待支付
        self.login_wechat()   #微信登录

    def cat_wait_send(self):
        '''查看待配送'''
        self.click_mine()      #点击我的
        self.click_wait_send() #点击待配送
        self.login_wechat()    #微信登录

    def cat_send(self):
        '''查看配送中'''
        self.click_mine()     #点击我的
        self.click_send()     #点击待配送
        self.login_wechat()   #点击微信登录

    def cat_evaluate(self):
        '''查看待评价'''
        self.click_mine()     #点击我的
        self.click_evaluate() #点击待评价
        self.login_wechat()   #微信登录

    def cat_refund(self):
        '''查看售后'''
        self.click_mine()     #点击我的
        self.click_refund()   #点击售后
        self.login_wechat()   #点击微信登录

