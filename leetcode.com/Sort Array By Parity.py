# https://leetcode.com/problems/sort-array-by-parity/

def sort_array_by_parity(self, nums: list[int]) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        if not nums[l] & 1:
            l += 1
        elif nums[r] & 1:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    return nums
