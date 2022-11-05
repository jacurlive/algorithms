# def sort_double(s):
#     c = 0
#     l = len(s)
#     has_zero = False
#     for i in range(l // 2):
#         if s[l - i - 1] == '0':
#             has_zero = True
#         if s[i] > s[l - i - 1]:
#             c += 1
#     return c
#
#
# a = '000101'
# sort_double(a)

# def solution(head: list):
#     l, r = 0, len(head) - 1
#     while r and l < r:
#         if head[l] == head[r]:
#             head.pop(l)
#             head.pop(r)
#
#         r += 1
#         l += 1
#     return head
#
#
# a = [1, 2, 2, 3, 3, 4, 5]
# print(solution(a))


# class MyHashSet:
#
#     def __init__(self):
#         self.d = {}
#
#     def add(self, key: int):
#         self.d = {
#             key
#         }
#
#     def remove(self, key: int):
#         self.d.pop(key)
#
#     def contains(self, key: int):
#         if key in self.d:
#             return True
#         return False

# a = [1, 2, 4, 5, 2, 6, 7]
# b = [8, 3, 5]
#
# r = len(a) - len(b)
#
# print(a[:r] + b)

# a = [3, 1, 4, 2, 4, 6, 8, 9, 11, 14, 15, 18, 1]
#
#
# def sort_f(s):
#     for i in range(len(s) - 1):
#         for j in range(1, len(s)):
#             # print(i, j)
#             if s[j] < s[j - 1]:
#                 s[j - 1], s[j] = s[j], s[j - 1]
#     return s
#
#
# print(sort_f(a))
