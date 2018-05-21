#coding=utf-8
import time
import itchat
from mail_sender import MailSender
from fund_getter import FundGetter

amount001008=925.06
amount040008=1841.41
amount005216=2520.13
amount005612=2991.91
amount005644=1003.87
my_sender='XXX@qq.com'
my_pass = 'XXX'	
receiver_addr=['XXX@live.com']
sender_name='FundCalculator'
subject='DailyFund'
wechat_switch=0  #wechat_switch设置为1时，发送微信消息，否则仅发送邮件通知

def cal(status,extent,amount):
	result = extent * amount
	return result

def get_daily_result(fundcode,amount):
	fundgetter=FundGetter(fundcode)
	status,worth,extent=fundgetter.get_price()
	result = extent * amount
	return result

def get_time():
	CurrentHour=int(time.strftime('%H',time.localtime(time.time())))
	CurrentMin=int(time.strftime('%M',time.localtime(time.time())))
	CurrentTime=CurrentHour+CurrentMin/100
	CurrentWeek=int(time.strftime('%w',time.localtime(time.time())))
	return CurrentTime,CurrentWeek

while 1:
	CurrentTime,CurrentWeek=get_time()
	if CurrentWeek!=0 and CurrentWeek!=6:
		result001008=get_daily_result('001008',amount001008)
		amount001008=amount001008+result001008
		result040008=get_daily_result('040008',amount040008)
		amount040008=amount040008+result040008
		result005216=get_daily_result('005216',amount005216)
		amount005216=amount005216+result005216
		result005612=get_daily_result('005612',amount005612)
		amount005612=amount005612+result005612
		result005644=get_daily_result('005644',amount005644)
		amount005644=amount005644+result005644
		result = result001008 + result040008 + result005612 + result005644
		print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '合计：'+ str(result))
		if result>0:
			content=("今日收涨，盈利%s元" %(result))
		else:
			content=("今日收跌，亏损%s元" %(-result))
		mailsender=MailSender(my_sender,my_pass,sender_name,receiver_addr,subject,content)
		if wechat_switch==1:
			itchat.send((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+content),'filehelper')
			print((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+'微信消息发送成功')
		else:
			print((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+'微信消息开关为关,仅发送邮件')
		mailsender.send_it()
		print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '一天后重发')
		time.sleep(86400)
	else:
		print((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+'当前为星期%s非交易日，六小时后重试'%(CurrentWeek))
		time.sleep(21600)
print('程序终止')