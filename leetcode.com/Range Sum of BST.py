# https://leetcode.com/problems/range-sum-of-bst/

class Solution:
    def range_sum_bst(self, root, low: int, high: int) -> int:
        if root:
            return self.range_sum_bst(root.left, low, high) + self.range_sum_bst(root.right, low, high) + root.val * (
                        low <= root.val <= high)
        return 0
