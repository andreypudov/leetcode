# 380. Insert Delete GetRandom O(1)
#
# Implement the RandomizedSet class:
#
#    - RandomizedSet() Initializes the RandomizedSet object.
#    - bool insert(int val) Inserts an item val into the set if not present.
#      Returns true if the item was not present, false otherwise.
#    - bool remove(int val) Removes an item val from the set if present.
#      Returns true if the item was present, false otherwise.
#    - int getRandom() Returns a random element from the current set of
#      elements (it's guaranteed that at least one element exists when this
#      method is called). Each element must have the same probability of being
#      returned.
#
# You must implement the functions of the class such that each function works
# in average O(1) time complexity.


import random


class RandomizedSet:

    def __init__(self):
        self.items = list()
        self.positions = dict()
        self.rng = random.Random(42)

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        else:
            self.items.append(val)
            self.positions[val] = len(self.items) - 1

            return True

    def remove(self, val: int) -> bool:
        if val in self.positions:
            position = self.positions[val]
            last_val = self.items[-1]

            self.items[position] = last_val
            self.positions[last_val] = position

            self.items.pop()
            del self.positions[val]

            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.rng.choice(self.items)
