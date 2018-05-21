#coding=utf-8

import time
import itchat
from bs4 import BeautifulSoup
from mail_sender import MailSender
from fund_getter import FundGetter



fundgetter=FundGetter('040008')
status,worth,up_and_downs=fundgetter.get_price()
print(status,worth,up_and_downs)