# coding=utf-8
import time
import itchat
from mail_sender import MailSender
from fund_getter import FundGetter
from data_controller import DataController

funds = ['001008', '040008', '005612', '005644']

amounts = [0, 0, 0, 0]

my_sender = 'XXX@qq.com'
my_pass = 'XXX'
receiver_addr = ['XXX@live.com']
sender_name = 'FundCalculator'
subject = 'DailyFund'
wechat_switch = 0  # wechat_switch设置为1时，发送微信消息，否则仅发送邮件通知


def get_daily_result(fundcode, amount):
    print('获取' + fundcode + '净值...')
    fundgetter = FundGetter(fundcode)
    today_fund_price, extent = fundgetter.get_price()
    dc = DataController()
    yesterday_fund_price = float(dc.get_fund_price(fundcode))
    result = extent * float(amount)
    return today_fund_price, result


def get_time():
    CurrentHour = int(time.strftime('%H', time.localtime(time.time())))
    CurrentMin = int(time.strftime('%M', time.localtime(time.time())))
    CurrentTime = CurrentHour + CurrentMin / 100
    CurrentWeek = int(time.strftime('%w', time.localtime(time.time())))
    return CurrentTime, CurrentWeek

# itchat.auto_login(hotReload=True)
dc = DataController()
dc.create_table()
if dc.if_data_need_to_init(len(funds)):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '表中没有数据，需要初始化数据')
    dc.clean_data()
    i = 0
    for fund in funds:
        dc.init_data(funds[i])
        i += 1
else:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '表中已经存在数据，无需初始化，表中的基金份额为：')
    for fund in funds:
        print(fund + '的份额为: ' + str(round(dc.get_fund_amount(fund), 2)))
    y_or_n = input(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '是否需要重新确定份额？Y/N')
    if y_or_n == 'Y' or y_or_n == 'y':
        dc.clean_data()
        i = 0
        for fund in funds:
            dc.init_data(funds[i])
            i += 1
    else:
        pass
y_or_n = input(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '是否需要根据当前涨跌重新计算份额并更新数据库？Y/N')
if y_or_n == 'Y' or y_or_n == 'y':
    pass
else:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '一天后开始更新并发送邮件')
    time.sleep(86400)

while 1:
    CurrentTime, CurrentWeek = get_time()
    if CurrentWeek != 0 and CurrentWeek != 6:
        fund_price = [0, 0, 0, 0, 0]
        result = [0, 0, 0, 0, 0]
        i = 0
        for amount in amounts:
            amounts[i] = dc.get_fund_amount(funds[i])
            i += 1
        i = 0
        for fund in funds:
            fund_price[i], result[i] = get_daily_result(funds[i], amounts[i])
            new_amount = float(amounts[i]) + float(result[i])
            amounts[i] = new_amount
            print('开始保存...')
            dc.update_data(funds[i], fund_price[i], amounts[i])
            i += 1
        finalresult = sum(result)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '合计：' + str(round(finalresult, 2)))
        if finalresult > 0:
            content = ("今日收涨，盈利%s元" % round((finalresult), 2)
        else:
            content=("今日收跌，亏损%s元" % round((-finalresult), 2))
        mailsender=MailSender(my_sender, my_pass, sender_name, receiver_addr, subject, content)
        if wechat_switch == 1:
            itchat.send((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + content), 'filehelper')
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '微信消息发送成功')
        else:
            print((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + '微信消息开关为关,仅发送邮件')
        mailsender.send_it()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '一天后重发')
        time.sleep(86400)
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '当前为星期%s非交易日，六小时后重试' % (CurrentWeek))
        time.sleep(21600)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '程序终止')
