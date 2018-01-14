import os, json, sys
def get_zhuyao(select):
    members=select.xpath('//div[@id="_container_staff"]//div[@class="staffinfo-module-container"]')
    temp={}
    for m in members:
        temp[m.xpath('./div/div/span/text()').extract_first()] = \
            m.xpath('./div/a/text()').extract_first()
    return temp