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
