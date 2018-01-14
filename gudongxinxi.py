import os, json, sys
import scrapy
def get_gudong(selecter):
    trs=selecter.xpath('//div[@id="_container_holder"]//tbody/tr')
    Ltemp=[]
    for t in trs:
        temp = {}
        temp['股东']=t.xpath('./td[1]/a/text()').extract_first()
        temp['出资比例']=t.xpath('./td[2]//span/text()').extract_first()
        temp['认缴出资']=t.xpath('./td[3]//span/text()').extract_first()
        Ltemp.append(temp)
    return Ltemp