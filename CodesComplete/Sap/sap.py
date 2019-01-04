"""
Sap GUI scripting class on Python
Created on 21 December 2018
@vinimmelo - Vinícius Melo
"""

import sys, win32com.client, time

class Sap:
    """ Sap Gui Scripting Class"""
    def __init__(self, transaction):
        try:
            self._SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
            self._session = self._SapGui.FindById("ses[0]")
            self._transaction = transaction
            self.initialize(transaction)
        except Exception as ex:
            raise ConnectionError("Session or Sap Gui Connection Error")

    @property
    def transaction(self):
        return self._transaction

    def initialize(self, transaction):
        self._session.findById("wnd[0]").maximize
        self._session.findById("wnd[0]/tbar[0]/okcd").text = "/n" + transaction
        self._session.findById("wnd[0]").sendVKey(0)

    def find_by_id(self, code):
        self._time()
        return self._session.findById(code)

    def press(self, code):
        self._time()
        self._session.findById(code).Press()

    def _time(self):
        time.sleep(0.15)
