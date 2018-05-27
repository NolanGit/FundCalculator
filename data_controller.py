import mysql.connector
import time


class DataInitializer(object):

<<<<<<< HEAD
=======
    def __init__(self):
        self.log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757
    def init_data(self, fund_code):
        fund_amount = input('请输入%s的持有量：' % fund_code)
        current_date = time.strftime('%Y%m%d', time.localtime(time.time()))
        fund_price = 0
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('insert into fund_data (fund_code,date,fund_price,fund_amount) values (%s, %s, %s, %s)', [fund_code, current_date, fund_price, fund_amount])
        conn.commit()
        cursor.close()
<<<<<<< HEAD
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '数据初始化成功')
=======
        print(self.log_time + '数据初始化成功')
>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757


class DataStorager(object):

<<<<<<< HEAD
=======
    def __init__(self):
        self.log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757
    def create_table(self):
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('create table if not exists fund_data (fund_code varchar(20), date varchar(20),fund_price varchar(20),fund_amount varchar(20))')
        conn.commit()
        cursor.close()
<<<<<<< HEAD
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '建表成功')
=======
        print(self.log_time + '建表成功')
>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757

    def save_data(self, fund_code, fund_price, fund_amount):
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        current_date = time.strftime('%Y%m%d', time.localtime(time.time()))
        cursor.execute('insert into fund_data (fund_code,date,fund_price,fund_amount) values (%s, %s, %s, %s)', [fund_code, current_date, fund_price, fund_amount])
        conn.commit()
        cursor.close()
<<<<<<< HEAD
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '保存数据成功')
=======
        print(self.log_time + '保存数据成功')
>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757


class DataGetter(object):

<<<<<<< HEAD
=======
    def __init__(self):
        self.log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757
    def get_data(self, fund_code):
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('select fund_amount from fund_data where fund_code = %s', [fund_code])
        fund_amount = cursor.fetchone()
        for fund_am in fund_amount:
            fund_amount = fund_am
        return fund_amount
        conn.commit()
        cursor.close()
<<<<<<< HEAD
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '保存数据成功')
=======
        print(self.log_time + '保存数据成功')
>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757


class DataCleanner(object):

<<<<<<< HEAD
=======
    def __init__(self):
        self.log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757
    def clean_data(self):
        conn = mysql.connector.connect(user='root', password='root', database='mydatabase')
        cursor = conn.cursor()
        cursor.execute('delete from fund_data')
        conn.commit()
        cursor.close()
<<<<<<< HEAD
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '数据库已清空')
=======
        print(self.log_time + '数据库已清空')
>>>>>>> e83f90fa72ffc2786ba8f32d2d35e7ef16f69757
