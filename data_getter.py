import mysql.connector
import time


class DataGetter(object):

    def __init__(self):
        self.log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

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
        print(self.log_time + '保存数据成功')
