import mysql.connector
import time


class DataController(object):

    def init_data(self, fund_code):
        # 初始化数据
        fund_amount = input('请输入%s的持有量：' % fund_code)
        current_date = time.strftime('%Y%m%d', time.localtime(time.time()))
        fund_price = 0
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('insert into fund_data (fund_code,date,fund_price,fund_amount) values (%s, %s, %s, %s)', [fund_code, current_date, fund_price, fund_amount])
        conn.commit()
        cursor.close()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '数据初始化成功')

    def create_table(self):
        # 建表
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('create table if not exists fund_data (fund_code varchar(20), date varchar(20),fund_price varchar(20),fund_amount varchar(20))')
        conn.commit()
        cursor.close()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '建表成功')

    def save_data(self, fund_code, fund_price, fund_amount):
        # 保存数据
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        current_date = time.strftime('%Y%m%d', time.localtime(time.time()))
        cursor.execute('insert into fund_data (fund_code,date,fund_price,fund_amount) values (%s, %s, %s, %s)', [fund_code, current_date, fund_price, fund_amount])
        conn.commit()
        cursor.close()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '保存数据成功')

    def get_fund_amount(self, fund_code):
        # 获取基金份额
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('select fund_amount from fund_data where fund_code = %s', [fund_code])
        fund_amount = cursor.fetchone()
        for fund_am in fund_amount:
            fund_amount = fund_am
        cursor.close()
        return float(fund_amount)

    def get_fund_price(self, fund_code):
        # 获取基金净值
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('select fund_price from fund_data where fund_code = %s', [fund_code])
        fund_price = cursor.fetchone()
        for fund_pr in fund_price:
            fund_price = fund_pr
        cursor.close()
        return fund_price

    def clean_data(self):
        # 删表
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('delete from fund_data')
        conn.commit()
        cursor.close()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '数据库已清空')

    def update_data(self, fund_code, fund_price, fund_amount):
        # 更新数据
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        current_date = time.strftime('%Y%m%d', time.localtime(time.time()))
        cursor.execute('UPDATE fund_data SET date=%s,fund_price=%s,fund_amount=%s WHERE fund_code=%s', [current_date, fund_price, fund_amount, fund_code])
        conn.commit()
        cursor.close()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '数据库已更新')

    def if_data_need_to_init(self, length):
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('select count(*) from fund_data')
        status = cursor.fetchone()
        conn.commit()
        cursor.close()
        if status[0] != length:
            return True
        else:
            return False

    def get_current_fund_code(self):
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('select fund_code from fund_data')
        fund_codes = cursor.fetchone()
        fund_code = []
        for each_fund_code in fund_codes:
            fund_code.append(each_fund_code)
            print(each_fund_code)
        cursor.close()
        return fund_code
