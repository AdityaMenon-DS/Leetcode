class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        x = targetSum - root.val

        return (
            self.hasPathSum(root.left, x) or
            self.hasPathSum(root.right, x)
        )