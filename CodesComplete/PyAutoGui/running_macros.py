"""
Running excel macros directly from Python. Yeah!
Created on 04 January 2019
@vinimmelo - Vinícius Melo
"""

import win32com.client
import os


def run_macro(filename: str, macro_name: str):
    """
    Run macro inside excel.
    Usage Example: run_macro(r'C:/Users/brmelovi/Desktop/Demand Capture Colombia.xlsb', 'Main.teste')
    """
    if os.path.exists(filename):
        xl=win32com.client.Dispatch('Excel.Application')
        xl.Workbooks.Open(Filename=filename, ReadOnly = True)
        xl.Application.Run(macro_name)
        xl.DisplayAlerts = False
        xl.Application.Quit()
        del xl
        print("Macro Finished!")
    else:
        print(f"Filename don't exist!\nPlease verify >> {filename} ")

import os
def open_programs():
    """
    Open a program with his default value, in case the file are attached to some extension, like pdf, xls, doc
    """
    import subprocess
    subprocess.Popen(['start', os.path.abspath('C:\\Windows\\System32\\calc.exe')], shell=True)


def hello():
    return print('Hey, worked!!!')

from apscheduler.schedulers.blocking import BlockingScheduler

def waiting_to_processing():
    sched = BlockingScheduler()
    sched.add_job(open_programs, 'interval', seconds=5)
    sched.add_job(open_programs, 'interval', seconds=15)
    sched.add_job(hello, 'interval', seconds=2)
    sched.start()


def test_running_two_macros():
    pass


if __name__ == '__main__':
    test_running_two_macros()
