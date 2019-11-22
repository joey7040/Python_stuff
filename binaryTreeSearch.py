class Solution:
    def isvalidBST(self, root:TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root, float('-inf'), float('inf'))
