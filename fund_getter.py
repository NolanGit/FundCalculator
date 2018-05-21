#coding=utf-8
import requests
import time
from bs4 import BeautifulSoup

class FundGetter():

	def __init__(self,fundcode):
		self.fundcode=fundcode
		
	def get_price(self):
		while 1:
			baseurl='http://so.hexun.com/default.do?type=fund&key='
			r = requests.get(baseurl+str(self.fundcode))
			time.sleep(5)  #避免网速低而加载过慢
			content=r.text
			soup = BeautifulSoup(content, 'lxml') 
			divs=soup.find_all(class_='red')
			if divs == None:
				divs=soup.find_all(class_='green')
				if divs == None:
					print('获取失败，记录错误...')
					print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'logging error...')
					with open('C:\\Users\\sunhaoran\\Documents\\fund_log.txt','a',encoding='UTF-8')as f:
						f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
						f.write(str(soup))
						f.write('============================================================')
					print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'logged...')
					print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'数据获取失败，五分钟后将重试')
					time.sleep(300)
				else:
					status=0  #0代表DOWN
					break
			else:
				status=1  #1代表UP
				break
		worth=divs[0].get_text()
		up_and_downs=divs[1].get_text()
		return status,worth,up_and_downs


fundgetter=FundGetter('040008')
status,worth,up_and_downs=fundgetter.get_price()
print(status,worth,up_and_downs)