# https://binarysearch.com/problems/Range-Query-on-a-List
class RangeSum:
    def __init__(self, nums):
        self.nums = nums

    def total(self, i, j):
        return sum(self.nums[i:j])


r = RangeSum([1, 2, 5, 0, 3, 7, 6, 4, 12, 435, 54, 34, 5, 324, 43, 34, 34])
print(r.total(1, 13))
