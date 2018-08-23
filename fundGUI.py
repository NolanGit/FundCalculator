# coding = utf-8
import os
import time
import queue
import shutil
import pyforms
import traceback
import threading
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlLabel
from pyforms.controls import ControlTextArea
from data_controller import DataController
from fund_getter import FundGetter
q1 = queue.Queue()
lock = threading.Lock()
dc = DataController()
fg = FundGetter()


class FundCalculatorGUI(BaseWidget):

    def __init__(self):
        super(FundCalculatorGUI, self).__init__('FundCalculatorGUI')

        self.daily_report = ControlLabel()

        self.current_fund = ControlLabel('Current Fund:')
        self.fund_code = ControlText('Fund Code:')
        self.fund_amount = ControlText('Fund Amount:')
        self.add_fund_button = ControlButton('Add Fund')
        self.add_fund_button.value = self.add_fund

        self.sender_address = ControlText('Sender Address:')
        self.sender_password = ControlText('Sender Password:')
        self.receiver_address = ControlText('Receiver Address:')

        self.current_status_label = ControlLabel('Current Status:')
        self.current_status = ControlLabel(time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())) + ' Program is not running...' + ' ' * 10)

        self.button = ControlButton('OK')
        self.button.value = self.button_action

        self.set_margin(15)
        self.formset = [{
            'Daily Report': ['daily_report'],
            'Fund List':['current_fund', ('fund_code', 'fund_amount'), 'add_fund_button'],
            'Settings':[('sender_address', 'sender_password'), 'receiver_address', ('current_status_label', 'current_status'), 'button']
        }]

    def button_action(self):
        self.current_status.value = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())) + '  Program is running...' + ' ' * 10
        get_current_fund_thread = threading.Thread(target=self.get_current_fund)
        get_current_fund_thread.start()
        get_current_fund_thread.join()
        current_fund = list()
        current_fund.append(q1.get())
        lock.acquire()
        self.current_fund.value = current_fund[0]
        lock.release()

    def get_current_fund(self):
        current_fund_code = str(dc.get_current_fund_code())
        q1.put('Current Funds are :' + current_fund_code)

    def add_fund(self):
        target_fund_code = self.fund_code.value
        target_fund_amount = self.fund_amount.value


if __name__ == "__main__":
    pyforms.start_app(FundCalculatorGUI)
