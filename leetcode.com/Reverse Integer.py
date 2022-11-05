# https://leetcode.com/problems/reverse-integer/

def reverse(self, x: int) -> int:
    reversed_num = 0
    if x < 0:
        x = abs(x)
        while x != 0:
            reversed_num = (10 * reversed_num) + x % 10

            x = x // 10
        return 0 if -(reversed_num) < -2 ** 31 else -(reversed_num)
    else:
        while x != 0:
            reversed_num = (10 * reversed_num) + x % 10

            x = x // 10
        return 0 if reversed_num > 2 ** 31 - 1 else reversed_num
