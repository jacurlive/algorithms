# https://leetcode.com/problems/guess-number-higher-or-lower/

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) >> 1
            if guess(mid) == -1:
                r = mid - 1
            elif guess(mid) == 1:
                l = mid + 1
            elif guess(mid) == 0:
                return mid