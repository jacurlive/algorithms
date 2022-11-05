# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def remove_duplicates(nums: list[int]) -> int:
    i = 0
    for j in nums:
        if j not in nums[:i]:
            nums[i] = j
            i += 1
    return i
