#coding=utf-8

import time
import itchat
from bs4 import BeautifulSoup
from mail_sender import MailSender
from fund_getter import FundGetter


my_sender='XXX@qq.com'
my_pass='XXXXXX'
ReceiverAddr=['XXX@live.com']
SenderName='FundCalculator'
Subject='DailyFund'

MailSender=MailSender(my_sender,my_pass,SenderName,ReceiverAddr,Subject,Content)
MailSender.SendIt()
fundgetter040008=FundGetter('040008')
status,worth,extent=fundgetter.get_price()
if status==0:
	status='今天收跌'
else:
	status='今天收涨'
