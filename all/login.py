import os, json, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def login():
    # chrome无头模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    path='/home/lyg/chromedriver_linux64/chromedriver'
    # driver=webdriver.Chrome(path,chrome_options=chrome_options)
    driver=webdriver.Chrome(path)

    # 登录
    driver.get('https://www.tianyancha.com/login')
    # \换行,contains有s
    phone=driver.find_element_by_xpath('//div[contains(@class,"modulein modulein1")]\
                                 //div[@class="pb30 position-rel"]//input')
    password=driver.find_element_by_xpath('//div[contains(@class,"modulein modulein1")]\
                                 //div[@class="pb40 position-rel"]//input')
    phone.send_keys('17602134795')
    password.send_keys('lyg4795lyg')
    ensure=driver.find_element_by_xpath('//div[contains(@class,"modulein modulein1")]'
                                        '//div[@onclick="loginByPhone(event);"]')
    # ensure = driver.find_element_by_xpath('//div[contains(@class,"modulein modulein1")]\
    #                                  //div[@onclick="loginByPhone(event);"]')
    ensure.click()
    return driver
