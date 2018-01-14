import os, json, sys
import time
import scrapy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 需要界面内点击下一页的要driver参数
def get_rongzi(selecter,driver):
    Ltemp = []
    while True:
        trs = selecter.xpath('//div[@id="_container_rongzi"]//tbody/tr')

        for t in trs:
            temp = {}
            temp['时间'] = t.xpath('./td[1]/span/text()').extract_first()
            temp['轮次'] = t.xpath('./td[2]/span/text()').extract_first()
            temp['估值'] = t.xpath('./td[3]/span/text()').extract_first()
            temp['金额'] = t.xpath('./td[4]/span/text()').extract_first()
            temp['比例'] = t.xpath('./td[5]/span/text()').extract_first()
            temp['投资方'] = t.xpath('./td[6]/span/a/text()').extract()
            temp['新闻来源'] = t.xpath('./td[7]/span/a/@href').extract_first()
            temp['新闻简介'] = t.xpath('./td[7]/span/a/text()').extract_first()
            Ltemp.append(temp)
        try:
            driver.find_element_by_xpath('//div[@id="_container_rongzi  "]'
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

