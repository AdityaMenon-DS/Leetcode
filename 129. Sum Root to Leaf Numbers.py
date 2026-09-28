class Solution(object):
    def sumNumbers(self, root):
        def f(node, x):
            if not node:
                return 0

            x = x * 10 + node.val

            if not node.left and not node.right:
                return x

            return f(node.left, x) + f(node.right, x)

        return f(root, 0)