class Solution(object):
    def maxPathSum(self, root):
        ans = [float('-inf')]

        def f(node):
            if not node:
                return 0

            l = max(0, f(node.left))
            r = max(0, f(node.right))

            ans[0] = max(ans[0], node.val + l + r)

            return node.val + max(l, r)

        f(root)
        return ans[0]