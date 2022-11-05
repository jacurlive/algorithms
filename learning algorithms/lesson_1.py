# --- Line Sort
# nums = [2, 4, 1, 5, 24, 36, 57, 58]
#
# n = 24
#
# for i in nums:
#     if i == n:
#         print('Found')


# nums = [1, 2, 3, 4, 5, 24, 36, 57, 58, 59]
#
# target = 36
#
# left, right = 0, len(nums) - 1
# result = -1
#
# while left < right:
#     m = (left + right) // 2
#     if nums[m] == target:
#         result = m
#         break
#     elif nums[m] < target:
#         m += 1
#     else:
#         m -= 1
#
# print(result)

# nums = [1, 2, 3, 4, 5, 24, 36, 57, 58, 59]
#
# target = 36
#
# left, right = 0, len(nums)
# result = -1
#
# l, r = 0, len(nums) - 1
#
# for i in nums:
#     if l > r:
#         print('-1')
#     m = (l + r) // 2
#     if nums[m] == target:
#         print(m)
#         break
#     elif nums[m] < target:
#         m += 1
#     else:
#         m -= 1


# a = [23, 13, 43, 52, 25, 46, 58, 87, 98, 123, 144]
#
# for i in range(len(a)):
#     for j in range(1, len(a)-i):
#         if a[j] < a[j - 1]:
#             a[j - 1], a[j] = a[j], a[j - 1]
#
# print(a)
