class Solution(object):
    def pathSum(self, root, targetSum):
        ans = []
        path = []

        def f(node, total):
            if not node:
                return

            path.append(node.val)
            total += node.val

            if not node.left and not node.right:
                if total == targetSum:
                    ans.append(path[:])

            f(node.left, total)
            f(node.right, total)

            path.pop()

        f(root, 0)
        return ans