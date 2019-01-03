"""
Description
Created on 02 January 2019
@vinimmelo - Vinícius Melo
"""

import pyautogui as gui



class PyGuiAutomation:
    """
    Simple Py Auto Gui automation Class
    Initiate PAUSE and FAILSAFE to improve the behavior of pyautogui.
    Just create the class and use the modules.
    """
    def __init__(self):
        gui.PAUSE = 1
        gui.FAILSAFE = True
        self.width, self.height = gui.size()

    def gui(self):
        """ Just returns GUI object """
        return gui

    def moveTo(self, x, y, time=0.25):
        """Sample: moveTo(100, 100) """
        return gui.moveTo(x, y, duration=time)

    def moveRel(self, x, y):
        """Sample: moveRel(100, 100) """
        return gui.moveRel(x, y, duration=0.25)

    def position(self):
        """Sample: position(100, 100) """
        return gui.position()

    def click(self, x = None, y = None, button = 'left'):
        """Sample: click(100, 100, 'right') """
        return gui.click(x, y, button)

    def doubleClick(self, x = None, y = None):
        """Sample: doubleClick(100, 100) """
        return gui.doubleClick(x, y)

    def scroll(self, number):
        """Sample: scroll(200) """
        return gui.scroll(number)

    def typewrite(self, words, speed=0.1):
        """
        Sample 1: typewrite("Hey man, its working!!!")
        Sample 2: typewrite(['ctrl', 'c'])
        """
        return gui.typewrite(words, speed)
