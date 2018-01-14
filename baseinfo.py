import os, json, sys
import scrapy
def get_base(select):
    # 获取公司基本信息
    baseinfo = select.xpath('//div[@id="company_web_top"]')
    temp = {}
    temp['公司名称'] = baseinfo.xpath('.//div[@style="margin-left:20px;"]'
                                  '/div[@class="position-rel"]'
                                  '/span/text()').extract_first()
    temp['电话'] = baseinfo.xpath('.//div[@style="margin-left:20px;"]//div[@class="f14 sec-c2"]')[0]\
        .xpath('./div[1]/span[2]/text()').extract_first()
    temp['邮箱'] = baseinfo.xpath('.//div[@style="margin-left:20px;"]//div[@class="f14 sec-c2"]')[0]\
        .xpath('./div[2]/span[2]/text()').extract_first()
    temp['网址'] = baseinfo.xpath('.//div[@style="margin-left:20px;"]//div[@class="f14 sec-c2"]')[1]\
        .xpath('./div[1]/a/text()').extract_first()
    temp['地址'] = baseinfo.xpath('.//div[@style="margin-left:20px;"]//div[@class="f14 sec-c2"]')[1] \
        .xpath('./div[2]/span[2]/text()').extract_first()
    # 简介要获取详情页里面的内容
    temp['简介'] = baseinfo.xpath('//*[@id="company_base_info_detail"]//text()').extract_first()
    return temp