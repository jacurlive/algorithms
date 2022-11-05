# def binary_search(nums, target):
#     left, right = 0, len(nums) - 1
#     result = -1
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             result = mid
#             break
#         elif nums[mid] < target:
#             left += 1
#         else:
#             right -= 1
#     return result
#
#
# a = [1, 3, 4, 5, 6, 8, 9, 11, 14, 15, 16, 18, 20, 21, 22, 26]
# tar = 22
#
# print(binary_search(a, tar))

# a = [23, 13, 43, 52, 25, 46, 58, 87, 98, 123, 144, 1]
#
# for i in range(len(a)):
#     for j in range(1, len(a)-i):
#         if a[j] < a[j - 1]:
#             a[j - 1], a[j] = a[j], a[j - 1]
#
# print(a)
# from random import randrange
#
#
# def quick_sort(a):
#     if len(a) < 2:
#         return a
#
#     pilot = a.pop(randrange(len(a)))
#     left = [i for i in a if i < pilot]
#     right = [i for i in a if i > pilot]
#
#     return quick_sort(left) + [pilot] + quick_sort(right)
#
#
# a = [23, 13, 43, 52, 25, 46, 58, 87, 98, 123, 144, 1]
#
# print(quick_sort(a))

# def two_sum(nums: list, target: int) -> list:
#     for i in range(len(nums)):
#         m = target - nums[i]
#
#         if m in nums and nums.index(m) != i:
#             return [nums.index(m), i]


#
# nums = [3, 2, 4]
# target = 6
#
# print(two_sum(nums, target))

# x = 0
#
#
# def is_palindrome(x: int):
#     if x < 0:
#         return False
#     return str(x) == str(x)[::-1]
#
#
# print(is_palindrome(x))

# def length_word(s: str) -> int:
#     return len(s.strip().split(' ')[-1])
#
#
# s = 'Hello World'
# print(length_word(s))

# def remove_duplicate(arr: list) -> int:
#     i = 0
#     for j in arr:
#         if j not in arr[:i]:
#             arr[i] = j
#             i += 1
#     return i
#
#
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#
# print(remove_duplicate(nums))

# def is_valid(s: str) -> bool:
#     stack, hm = [], {'(': ')', '{': '}', '[': ']'}
#     for ch in s:
#         if ch in hm:
#             stack.append(ch)
#         else:
#             if not stack or hm[stack[-1]] != ch:
#                 return False
#             stack.pop()
#
#     return not stack
#
#
# s = "()[]{"
#
# print(is_valid(s))

# def reverse_number(x: int) -> int:
#     reversed_num = 0
#     if x < 0:
#         x = abs(x)
#         while x != 0:
#             curr_digit = x % 10
#             reversed_num = 10*reversed_num
#             reversed_num = reversed_num + curr_digit
#
#             x = x // 10
#         return -(reversed_num)
#     else:
#         while x != 0:
#             curr_digit = x % 10
#             reversed_num = 10 * reversed_num
#             reversed_num = reversed_num + curr_digit
#
#             x = x // 10
#         return reversed_num
#
#
# n = -123
#
# # print(abs(n))
# print(reverse_number(n))

# def reverse(x: int) -> int:
#     reversed_num = 0
#     if x < 0:
#         x = abs(x)
#         while x != 0:
#             reversed_num = (10 * reversed_num) + x % 10
#
#             x = x // 10
#         return 0 if -(reversed_num) < -2 ** 31 else -(reversed_num)
#     else:
#         while x != 0:
#             reversed_num = (10 * reversed_num) + x % 10
#
#             x = x // 10
#         return 0 if reversed_num > 2 ** 31 - 1 else reversed_num
#
#
# n = 120
#
# print(reverse(n))

# def test(n: int):
#     k = -1
#     while n:
#         if n & 1 == k:
#             return False
#         k = n & 1
#         n >>= 1
#     return True
#
#
# c = 6
# # print(test(c))
# print(bin(c))

# def find_array(pref: list) -> list:
#     for i in range(len(pref) - 1, 0, -1):
#         pref[i] ^= pref[i - 1]
#     return pref
#
#
# pref1 = [5, 2, 0, 3, 1]
#
# print(find_array(pref1))

# def single_num(nums: list) -> list:
#     res = []
#     for i in nums:
#         if i not in res:
#             res.append(i)
#         else:
#             res.remove(i)
#     return res
#
#
# nums1 = [1, 2, 1, 3, 2, 5]
#
# print(single_num(nums1))

s = 8


# print(s & 1)

def sort_arr(nums: list) -> list:
    start, end = 0, len(nums) - 1
    while start < end:
        if nums[start] % 2 != 0 and nums[end] % 2 == 0:
            nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums


nums1 = [3, 1, 2, 4]

print(sort_arr(nums1))
