# https://leetcode.com/problems/search-in-a-binary-search-tree/

def search_bst(self, root, val: int):
    if not root or root.val == val:
        return root
    if val < root.val:
        return self.searchBST(root.left, val)
    return self.searchBST(root.right, val)
