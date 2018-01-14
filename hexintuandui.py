import os, json, sys
import time
import scrapy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 需要界面内点击下一页的要driver参数
def get_hexin(selecter,driver):
    Ltemp = []
    while True:
        members = selecter.xpath('//div[@id="_container_teamMember"]//div[@class="team-item"]')

        for t in members:
            temp = {}
            temp['名字'] = t.xpath('./div[1]/div[2]/text()').extract_first()
            temp['头像'] = t.xpath('./div[1]/div[1]/img/@src').extract_first()
            temp['头衔'] = t.xpath('./div[2]/div/text()').extract_first()
            # 资历有多段，因此不用extract_first()
            temp['资历'] = t.xpath('./div[2]/ul/li/span/text()').extract()
            Ltemp.append(temp)
        try:
            driver.find_element_by_xpath('//div[@id="_container_teamMember"]'
                                         '//div[@class="company_pager"]/ul'
                                    '/li[@class="pagination-next  "]/a').click()
            # 不等待的话界面还在加载但是程序已经继续执行，会导致第二页时候找不到element
            # time.sleep(3)
            # 显示等待当载入界面不存在时，界面会有一个下滑的过程，此时程序已经继续往下跑，会导致点击不到下一页
            # located里面要用元组形式
            WebDriverWait(driver, 20, 0.5).until_not(EC.presence_of_element_located((By.ID,"_loading_container")))
            time.sleep(1)
        except Exception as e:
            print(e)
            return Ltemp
        selecter=scrapy.Selector(text=driver.page_source)

