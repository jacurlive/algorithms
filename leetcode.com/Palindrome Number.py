# https://leetcode.com/problems/palindrome-number/

def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]
