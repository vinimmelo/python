"""
Sap GUI scripting on Python, based on: https://sappython.blogspot.com/
Created on 21 December 2018
@vinimmelo - Vinícius Melo
"""

import sys, win32com.client

def main():
    try:
        SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
        if not type(SapGui) == win32com.client.CDispatch:
           return print('Exit SapGui')

        session = SapGui.FindById("ses[0]")
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return print('Exit Session')

        session.findById("wnd[0]").resizeWorkingPane(173, 36, 0)
        session.findById("wnd[0]").maximize
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nfbl5n"
        session.findById("wnd[0]").sendVKey(0)
        print('The end!')
    except Exception as ex:
        print('Exception: ' + str(ex))
        print(sys.exc_info()[0])

    finally:
        session = None
        connection = None
        application = None
        SapGuiAuto = None


if __name__ == "__main__":
  main()
