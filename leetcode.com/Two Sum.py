# https://leetcode.com/problems/two-sum/

def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        m = target - nums[i]

        if m in nums and nums.index(m) != i:
            return [nums.index(m), i]
