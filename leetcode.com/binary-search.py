# https://leetcode.com/problems/binary-search/

def search(nums, target) -> int:
    result = -1
    left, right = 0, len(nums) - 1
    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            result = m
            break
        elif nums[m] < target:
            left = m + 1
        else:
            right = m - 1
    return result
