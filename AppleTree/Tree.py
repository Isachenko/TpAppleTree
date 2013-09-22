from AppleTree.Apple import Apple

__author__ = 'Isak'

import random

class Tree():
    def __init__(self):
        self.apples = []
        self.flowers = 0
        self.bloomed = False

    def grow(self):
        if not self.bloomed:
            print("There are no flowers in Tree")
            return
        self.bloomed = False
        count = self.flowers
        for i in range(0, count):
            self.apples.append(Apple())
        print("There are ", count, " apples on the tree")

    def shake(self):
        r = random.randint(0, len(self.apples))
        seedCount = 0
        for i in range(0, r):
            apple = self.apples.pop(0)
            seedCount += apple.seedCount
        print(r, " apples fall down")
        print(seedCount, " seeds fall down")
        print(len(self.apples), " still on the tree")

    def bloom(self):
        self.bloomed = True
        self.apples.clear()
        self.flowers = random.randint(1, 300)
        print("rose ", self.flowers, " flowers")

