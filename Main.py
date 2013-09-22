__author__ = 'andrew'

from AppleTree.Tree import *
from Menu.Menu import *

menu = Menu()

tree = Tree()

menu.addItem(MenuItem("Bloom", tree.bloom))
menu.addItem(MenuItem("Grow", tree.grow))
menu.addItem(MenuItem("Shake", tree.shake))

menu.show()



