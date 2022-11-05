# --- Selection Sort
# a = [2, 4, 1, 5, 6, 3, 11, 7, 14, 9]
#
#
# i, l = 0, len(a)
# while i < l:
#     minimum = i
#     j = i + 1
#     while j < l:
#         if a[minimum] > a[j]:
#             minimum = j
#         j += 1
#
#     a[i], a[minimum] = a[minimum], a[i]
#     i += 1
#
# print(a)


# --- Insertion Sort

# a = [2, 4, 1, 5, 6, 3, 11, 7, 14, 9]
#
# i = 1
#
# while i < len(a):
#     j = i
#     while j >= 0:
#         if a[i] < a[j]:
#             a[i], a[j] = a[j], a[i]
#             i -= 1
#         j -= 1
#     i += 1
#
# print(a)

# a = [2, 5, 8, 12, 16]
# b = [3, 4, 5, 7, 8, 9, 10]
# r = []
#
# while a and b:
#     if a[0] < b[0]:
#         r.append(a[0])
#         a.pop(0)
#     else:
#         r.append(b[0])
#         b.pop(0)
#
# r += a + b
# print(r)

# a = [2, 3, 4, 5, 6, 7, 8]
# b = [5, 4, 3, 2]
# print(hex(id(a)))
# s_1 = len(a)
# s_2 = len(b)
#
# r = (s_1 - s_2)
# print(a[:r] + b)


# a = [2, 4, 5, 6, 3, 11, 7, 14, 9, 1]
#
#
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[j] < a[i]:
#             a[j], a[i] = a[i], a[j]
#
# print(a)

from random import randrange


def quick_sort(s):
    if len(s) <= 1:
        return s

    mid = s.pop(randrange(len(s)))
    left = [i for i in s if i <= mid]
    right = [i for i in s if i > mid]
    # center = [i for i in s if i == mid]
    print(f'{left} + [{mid}] + {right}')

    return quick_sort(left) + [mid] + quick_sort(right)


a = [2, 4, 1, 5, 6, 3, 11, 7, -4, -1, 14, 9, 2]
print(quick_sort(a))
