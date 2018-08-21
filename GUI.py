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
q = queue.Queue()
lock = threading.Lock()


class FundCalculatorGUI(BaseWidget):

    def __init__(self):
        super(FundCalculatorGUI, self).__init__('FundCalculatorGUI')

        self.daily_report = ControlLabel()

        self.current_fund = ControlLabel('Current Fund:')
        self.fund_code = ControlText('Fund Code:')
        self.fund_amount = ControlText('Fund Amount:')
        self.add_fund_button = ControlButton('Add Fund')

        self.sender_address = ControlText('Sender Address:')
        self.sender_password = ControlText('Sender Password:')
        self.receiver_address = ControlText('Receiver Address:')

        self.current_status_label = ControlLabel('Current Status:')
        self.current_status = ControlLabel(time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())) + ' Program is not running...' + ' ' * 10)

        self.button = ControlButton('OK')

        self.set_margin(15)
        self.formset = [{
            'Daily Report': ['daily_report'],
            'Fund List':['current_fund', ('fund_code', 'fund_amount'), 'add_fund_button'],
            'Settings':[('sender_address', 'sender_password'), 'receiver_address', ('current_status_label', 'current_status'), 'button']
        }]
if __name__ == "__main__":
    pyforms.start_app(FundCalculatorGUI)
