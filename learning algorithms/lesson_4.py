from queue import Queue


class Node:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.value}'


def add(root, n):
    if not root:
        return Node(n)
    if root.value > n:
        root.left = add(root.left, n)
    else:
        root.right = add(root.right, n)
    return root


def pre_order(root):
    if not root:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value)


def res_print(root):
    space = ' '
    if not root:
        return
    print(space * 7, root.value)
    print(space * 5, '/', space, ' \ ')
    if root.left:
        print(space * 4, root.left, end='')
    if root.right:
        print(space * 3, root.right)


def bfs_print(root):
    queue = Queue()
    queue.put(root)
    l = depth(root)

    while not queue.empty():
        node = queue.get()
        print(node.value)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)


def depth(root):
    if not root:
        return 0
    else:
        left_side = depth(root.left)
        right_side = depth(root.right)

        return max(left_side, right_side) + 1


def is_balance(root):
    pass


low = 7
high = 15
s = 0


def range_sum(root):
    if not root:
        return
    if high >= root.value >= low:
        global s
        s += root.value
    if root.left:
        range_sum(root.left)
    if root.right:
        range_sum(root.right)
    return root


def maximum(root):
    if not root:
        return
    if root.right:
        return maximum(root.right)
    return root


def minimum(root):
    if not root:
        return
    if root.left:
        return minimum(root.left)
    return root


def right(root):
    while root.right or root.left:
        if root.right:
            root = root.right
        elif root.left:
            root = root.left
    return root


def left(root):
    while root.left or root.right:
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
    return root


def search_bst(root, val):
    if not root:
        return
    if root == val:
        return root
    if val < root.value:
        return search_bst(root.left, val)
    return search_bst(root.right, val)


root = None
list_1 = [5, 1, 7]

for i in list_1:
    root = add(root, i)

# print(maximum(root))
# print(minimum(root))
# print(right(root))
# print(left(root))

print(in_order(root))
