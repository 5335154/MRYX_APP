from selenium.webdriver.common.by import By

from base_page.adress import adress
from base_page.huwei_adress import hw_adress
from driver.huwei_driver import hw_driver


class PageAddGood():
    def __init__(self, driver):
        self.driver = driver
        self.loc_click_classify = (By.ID, 'cn.missfresh.application:id/classifyTab')
        self.loc_navigation = (By.ID, 'cn.missfresh.application:id/rv_top_label')
        self.loc_snacks =(By.XPATH, '//*[@text="肉蛋食材"]')
        self.loc_fruits = (By.XPATH, '//*[@text="时令水果"]')
        self.loc_click_seafood = (By.XPATH, '//*[@text="海鲜水产"]')
        self.loc_click_fish_classify = (By.ID, 'cn.missfresh.application:id/rlv_classify')
        self.loc_click_fish = (By.XPATH, '//*[@text="黄花鱼"]')
        self.loc_add_good = (By.ID, 'cn.missfresh.application:id/btn_main_item_buy_now')
        self.loc_cat_shopcard = (By.ID, 'cn.missfresh.application:id/cartTab')

    def click_classify(self):        #点击分类
        self.driver.find_element(*self.loc_click_classify).click()

    def swipe_to_fruits(self):      #将肉蛋食材移动到时令水果
        self.navigation = self.driver.find_element(*self.loc_navigation)
        snacks = self.navigation.find_element(*self.loc_snacks)
        fruits = self.navigation.find_element(*self.loc_fruits)
        self.driver.scroll(snacks, fruits)

    def click_seafood(self):        #点击海鲜水产
        self.navigation.find_element(*self.loc_click_seafood).click()

    def click_fish(self):           #点击黄花鱼
        classify = self.driver.find_element(*self.loc_click_fish_classify)
        classify.find_element(*self.loc_click_fish).click()

    def add_good(self):             #选择商品,添加至购物车
        page = self.driver.find_elements(*self.loc_add_good)
        page[0].click()

    def cat_shopcard(self):         #查看购物车
        self.driver.find_element(*self.loc_cat_shopcard).click()

    def page_add_good(self):
        self.click_classify()       #点击分类
        self.swipe_to_fruits()      #将休闲零食移动到时令水果
        self.click_seafood()        #点击海鲜水产
        self.click_fish()           #点击黄花鱼
        self.add_good()             #将商品直接添加至购物车
        self.cat_shopcard()         #查看购物车


