#coding=utf-8

import time
import itchat
from bs4 import BeautifulSoup
from mail_sender import MailSender
from fund_getter import FundGetter

amount001008=925.06
amount040008=1841.41
amount005216=2520.13
amount005612=2991.91
amount005644=1003.87

def cal(status,extent,amount):
	result = extent * amount
	return result

def calit(fundcode,amount):
	fundgetter=FundGetter(fundcode)
	status,worth,extent=fundgetter.get_price()
	result = extent * amount
	return result

result001008=calit('001008',amount001008)
print(result001008)

'''
#实现愚蠢，待优化
fundgetter001008=FundGetter('001008')
status001008,worth001008,extent001008=fundgetter001008.get_price()
result001008=cal(status001008,extent001008,amount001008)
amount001008=amount001008+result001008

fundgetter040008=FundGetter('040008')
status040008,worth040008,extent040008=fundgetter040008.get_price()
result040008=cal(status040008,extent040008,amount040008)
amount040008=amount040008+result040008

fundgetter005612=FundGetter('005612')
status005612,worth005612,extent005612=fundgetter005612.get_price()
result005612=cal(status005612,extent005612,amount005612)
amount005612=amount005612+result005612

fundgetter005644=FundGetter('005644')
status005644,worth005644,extent005644=fundgetter005644.get_price()
result005644=cal(status005644,extent005644,amount005644)
amount005644=amount005644+result005644

result = result001008 + result040008 + result005612 + result005644
print('合计：'+ str(result))
'''
'''
fundgetter=FundGetter('',)
status,worth,extent=fundgetter.get_price()
result=cal(status,extent,amount)
'''
'''
my_sender='XXX@qq.com'
my_pass='XXXXXX'
ReceiverAddr=['XXX@live.com']
SenderName='FundCalculator'
Subject='DailyFund'
MailSender=MailSender(my_sender,my_pass,SenderName,ReceiverAddr,Subject,Content)
MailSender.SendIt()
'''