# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

def find_array(pref: list) -> list:
    for i in range(len(pref) - 1, 0, -1):
        pref[i] ^= pref[i - 1]
    return pref
