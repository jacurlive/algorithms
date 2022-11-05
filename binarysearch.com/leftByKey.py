# https://binarysearch.com/problems/Rotate-List-Left-by-K
from collections import deque

nums = [1, 2, 3, 4, 5, 6]


def solve(nums):
    d = deque(nums)
    d.rotate(-2)
    d = list(d)
    return d


print(solve(nums))
