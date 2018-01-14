import os, json, sys
import time
import scrapy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 需要界面内点击下一页的要driver参数
def get_duiwai(selecter,driver):
    # nextpage=selecter.xpath('//div[@class="company_pager"]/ul/li/@class').extract()
    nextpage=''
    Ltemp = []
    while True:
        trs = selecter.xpath('//div[@id="_container_invest"]//tbody/tr')

        for t in trs:
            temp = {}
            temp['被投资公司名称'] = t.xpath('./td[1]/a/span/text()').extract_first()
            temp['被投资法定代表人'] = t.xpath('./td[2]/span/a/text()').extract_first()
            temp['注册资本'] = t.xpath('./td[3]/span/text()').extract_first()
            temp['投资数额'] = t.xpath('./td[4]/span/text()').extract_first()
            temp['投资占比'] = t.xpath('./td[5]/span/text()').extract_first()
            temp['注册时间'] = t.xpath('./td[6]/span/text()').extract_first()
            temp['状态'] = t.xpath('./td[7]/span/text()').extract_first()
            Ltemp.append(temp)
        try:
            driver.find_element_by_xpath('//div[@id="_container_invest"]'
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

