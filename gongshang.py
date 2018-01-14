import os, json, sys
import scrapy
def get_gongshang(select):
    trs=select.xpath('//div[@class="base0910"]/table//tr')
    temp={}
    for tr in trs[0:5]:
        temp[tr.xpath('./td[1]/text()').extract_first()]=\
            tr.xpath('./td[2]').xpath('string(.)').extract_first()
        temp[tr.xpath('./td[3]/text()').extract_first()] =\
            tr.xpath('./td[4]').xpath('string(.)').extract_first()
    temp[trs[5].xpath('./td[1]/text()').extract_first()] = \
        trs[5].xpath('./td[2]/text()').extract_first()

    detail_1=trs[6].xpath('.//span[@class="js-shrink-container"]/span[1]/text()').extract_first()
    detail_2=trs[6].xpath('.//span[@class="js-shrink-container"]/span[2]/text()').extract_first()
    # 经营范围可能存在两个位置，哪个全用哪个
    if detail_1>detail_2:
        temp['经营范围']=detail_1.strip('.')
    else:
        temp['经营范围'] = detail_2.strip('.')
    return temp