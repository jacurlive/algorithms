# https://leetcode.com/problems/design-hashset/

class MyHashSet:
    def __init__(self):
        self.s = set()

    def add(self, key: int):
        self.s.add(key)

    def remove(self, key: int):
        self.s.discard(key)

    def contains(self, key: int):
        return key in self.s
