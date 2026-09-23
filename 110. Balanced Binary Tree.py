class Solution(object):
    def isBalanced(self, root):

        def f(node):
            if not node:
                return 0

            l = f(node.left)
            if l == -1:
                return -1

            r = f(node.right)
            if r == -1:
                return -1

            if abs(l - r) > 1:
                return -1

            return 1 + max(l, r)

        return f(root) != -1