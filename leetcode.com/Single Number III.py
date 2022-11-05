# https://leetcode.com/problems/single-number-iii/

def single_num(nums: list) -> list:
    res = 0
    for ele in nums:
        res = res ^ ele

    rmsb = res & (-res)
    num1 = 0
    num2 = 0
    for ele in nums:
        if ele & rmsb != 0:
            num1 = num1 ^ ele
        else:
            num2 = num2 ^ ele
    return num1, num2
