# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

def has_alternating_bits(n: int) -> bool:
    k = -1
    while n:
        if n & 1 == k:
            return False
        k = n & 1
        n >>= 1
    return True
