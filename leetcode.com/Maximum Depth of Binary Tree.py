# https://leetcode.com/problems/maximum-depth-of-binary-tree/

def max_depth(self, root) -> int:
    if not root:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
