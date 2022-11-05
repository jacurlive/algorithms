# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


def get_value(head) -> int:
    s = ''
    tmp = head
    while head:
        s += str(tmp.val)
        tmp = tmp.next
    return int(s, 2)
