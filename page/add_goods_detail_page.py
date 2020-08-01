import time

from selenium.webdriver.common.by import By

from base_page.huwei_adress import hw_adress
from driver.huwei_driver import hw_driver


class AddGoods():
    def __init__(self, driver):
        self.driver = driver
        self.loc_click_classify = (By.ID, 'cn.missfresh.application:id/classifyTab')
        self.loc_click_subclassification = (By.XPATH, '//*[@text="西瓜"]')
        self.loc_click_good = (By.ID, 'cn.missfresh.application:id/tv_product_name')
        self.loc_add_shopcard_loction = (By.ID, 'cn.missfresh.application:id/ll_bottom_add_cart_bt')
        self.loc_add_shopcard = (By.XPATH, '//*[@text="加入购物车"]')
        self.loc_click_shopcard = (By.ID, 'cn.missfresh.application:id/iv_cart_icon')
        self.loc_click_buy_now_loction = (By.ID, 'cn.missfresh.application:id/ll_bottom_add_cart_bt')
        self.loc_click_buy_now = (By.XPATH, '//*[@text="立即购买"]')
        self.loc_cat_shopcard = (By.ID, 'cn.missfresh.application:id/iv_cart_icon')

    def click_classify(self):       #点击分类
        self.driver.find_element(*self.loc_click_classify).click()
        time.sleep(2)

    def click_subclassification(self):      #点击西瓜
        self.driver.find_element(*self.loc_click_subclassification).click()

    def click_good(self):           #点击第一个商品
        self.driver.find_element(*self.loc_click_good).click()

    def add_shopcard(self):         #详情点击加入购物车
        location = self.driver.find_element(*self.loc_add_shopcard_loction)
        location.find_element(*self.loc_add_shopcard).click()

    def click_shopcard(self):       #点击购物车图标查看
        self.driver.find_element(*self.loc_click_shopcard).click()

    def click_buy_now(self):        #点击立即购买
        location = self.driver.find_element(*self.loc_click_buy_now_loction)
        location.find_element(*self.loc_click_buy_now).click()

    def cat_shopcard(self):      #详情页面查看购物车
        self.driver.find_element(*self.loc_cat_shopcard).click()

    def in_good_details(self):
        '''进入商品详情页面'''
        self.click_classify()           #点击分类
        self.click_subclassification()  #点击西瓜
        self.click_good()               #点击商品

    def add_good_details(self):
        '''详情页面加入购物车并查看'''
        self.in_good_details()   #进入商品详情页面
        self.add_shopcard()      #点击加入购物车
        self.cat_shopcard()      #点击购物车查看购物车查看

    def buy_good_now(self):
        '''商品详情页面立即购买'''
        self.in_good_details()    #进入商品详情页面
        self.click_buy_now()      #点击立即购买




