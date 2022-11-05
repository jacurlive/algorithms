# https://leetcode.com/problems/delete-node-in-a-linked-list/

def delete_node(node, x):
    tmp = x
    while tmp:
        if tmp.val == node:
            pass
        else:
            print(tmp.val)
            tmp = tmp.next
