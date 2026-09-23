class Solution(object):
    def sortedArrayToBST(self, nums):

        def f(l, r):
            if l > r:
                return None

            m = (l + r) // 2

            root = TreeNode(nums[m])

            root.left = f(l, m - 1)
            root.right = f(m + 1, r)

            return root

        return f(0, len(nums) - 1)