# https://leetcode.com/problems/happy-number/

def is_happy(n: int) -> bool:
    if n > 9:
        res = 0
        r = [int(i) for i in str(n)]
        for i in r:
            res += i ** 2
        return is_happy(res)
    elif n == 1:
        return True
    else:
        return False
