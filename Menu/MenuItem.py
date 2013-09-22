__author__ = 'andrew'

class MenuItem:
    def __init__(self, text, func):
        self.text = text
        self.func = func

    def doFunc(self):
        self.func()

