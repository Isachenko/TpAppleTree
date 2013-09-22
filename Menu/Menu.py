__author__ = 'andrew'

from Menu.MenuItem import MenuItem

class Menu:
    def __init__(self):
        self.menuItems = []

    def addItem(self, menuItem):
        self.menuItems.append(menuItem)

    def show(self):
        i = 0
        print(i, ": Exit")
        for menuItem in self.menuItems:
            i += 1
            print(i, ": ", menuItem.text)

        opNum = int(input("Select: "))
        if type(opNum) != int or opNum < 0 or opNum > len(self.menuItems):
            print("Wrong Select")
            self.show()
            return
        if opNum == 0:
            return

        self.menuItems[opNum-1].doFunc()
        input("Pres eny key to continue...")
        self.show()
        return




