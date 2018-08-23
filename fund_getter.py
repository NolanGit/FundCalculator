# coding=utf-8
import requests
import time
from bs4 import BeautifulSoup


class FundGetter(object):

    def __init__(self, fundcode):
        self.fundcode = fundcode

    def get_price(self):
        while 1:
            baseurl = ('http://fund.eastmoney.com/%s.html' % (str(self.fundcode)))
            r = requests.get(baseurl)
            time.sleep(5)  # 避免网速低而加载过慢
            content = r.text
            soup = BeautifulSoup(content, 'lxml')
            divs = soup.find_all(class_='dataNums')
            print(divs)
            if divs == []or len(divs) != 3:
                print('获取失败，记录错误...')
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + 'logging error...')
                with open('C:\\Users\\sunhaoran\\Documents\\fund_log.txt', 'a', encoding='UTF-8')as f:
                    f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    f.write(str(soup))
                    f.write('=' * 50)
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + 'logged...')
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '数据获取失败，五分钟后将重试')
                time.sleep(300)
            else:
                break
        div = divs[1]
        num = div.get_text()
        num = str(num)
        worth = float(num[0:6])
        extent = float(num[6:10])
        extent = extent / 100
        return worth, extent
