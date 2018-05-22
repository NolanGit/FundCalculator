import mysql.connector
import time


class FundStorager(object):

	def __init__(self):
		self.log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def create_table(self):
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('create table if not exists fund_data (fund_code varchar(20) primary key, date varchar(20),fund_price varchar(20),fund_amount varchar(20))')
        cursor.close()
        print(self.log_time+'建表成功')

    def save_data(self, fund_code, fund_price,fund_amount):
        conn = mysql.connector.connect(user='root', password='root', database='mytest')
        cursor = conn.cursor()
        current_date = time.strftime('%Y%m%d', time.localtime(time.time()))
        cursor.execute('insert into fund_data (fund_code,date,fund_price,fund_amount) values (%s, %s, %s)', [fund_code, current_date, fund_price,fund_amount])
        conn.commit()
        cursor.close()
        print(self.log_time+'保存数据成功')

