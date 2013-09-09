__author__ = 'Isak'

import random, Apple


class Tree():
    def __init__(self):
        self.apples = []

    def grow(self):
        r = random.randint(1, 300)
        for i in range(0, r):
            self.apples.append(Apple.Apple())
        print("There are ", r, " apples on the tree")

    def shake(self):
        r = random.randint(0, len(self.apples))
        for i in range(0, r):
            self.apples.pop(0)
        print(r, " apples fall down")
        print(len(self.apples), " still on the tree")


tree = Tree()
tree.grow()
tree.grow()
tree.shake()
