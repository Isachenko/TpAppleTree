__author__ = 'jack'

import random, Apple


class Tree():
    def __init__(self):
        self.apples = []

    def grow(self):
        r = random.randint(3, 100)
        for i in range(0, r):
            self.apples.append(Apple.Apple())
        print("There are ", r, " apples on the tree")


tree = Tree()
tree.grow()
tree.grow()

