# coding=utf-8
import time
import itchat
from mail_sender import MailSender
from fund_getter import FundGetter
from data_controller import DataStorager, DataGetter, DataCleanner, DataInitializer

funds = ['001008', '040008', '005612', '005644']

amounts = [0, 0, 0, 0]

my_sender = 'XXX@qq.com'
my_pass = 'XXX'
receiver_addr = ['XXX@live.com']
sender_name = 'FundCalculator'
subject = 'DailyFund'
wechat_switch = 0  # wechat_switch设置为1时，发送微信消息，否则仅发送邮件通知


def get_daily_result(fundcode, amount):
    print(fundcode)
    fundgetter = FundGetter(fundcode)
    status, worth, extent = fundgetter.get_price()
    result = extent * float(amount)
    return worth, result


def get_time():
    CurrentHour = int(time.strftime('%H', time.localtime(time.time())))
    CurrentMin = int(time.strftime('%M', time.localtime(time.time())))
    CurrentTime = CurrentHour + CurrentMin / 100
    CurrentWeek = int(time.strftime('%w', time.localtime(time.time())))
    return CurrentTime, CurrentWeek

# itchat.auto_login(hotReload=True)
fs = DataStorager()
fs.create_table()
dg = DataGetter()
dc = DataCleanner()
di = DataInitializer()
i = 0
dc.clean_data()
for fund in funds:
    di.init_data(funds[i])
    i += 1

while 1:
    CurrentTime, CurrentWeek = get_time()
    if CurrentWeek != 0 and CurrentWeek != 6:
        fund_price = [0, 0, 0, 0, 0]
        result = [0, 0, 0, 0, 0]
        i = 0
        for amount in amounts:
            amounts[i] = dg.get_data(funds[i])
            i += 1
        dc.clean_data()
        i = 0
        for fund in funds:
            fund_price[i], result[i] = get_daily_result(funds[i], amounts[i])
            new_amount = float(amounts[i]) + float(result[i])
            amounts[i] = new_amount
            print('开始保存...')
            fs.save_data(funds[i], fund_price[i], amounts[i])
            i += 1

        finalresult = sum(result)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '合计：' + str(finalresult))
        if finalresult > 0:
            content = ("今日收涨，盈利%s元" % (finalresult))
        else:
            content = ("今日收跌，亏损%s元" % (-finalresult))
        mailsender = MailSender(my_sender, my_pass, sender_name, receiver_addr, subject, content)
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
print('程序终止')
