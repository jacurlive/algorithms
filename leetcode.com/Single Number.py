# https://leetcode.com/problems/single-number/

class Solution:
    def single_number(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
