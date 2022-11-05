# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def unique_occurrences(self, arr: list[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = 1 + d.get(i, 0)

        d = d.values()
        return len(d) == len(set(d))
