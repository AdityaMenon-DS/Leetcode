class Solution(object):
    def buildTree(self, inorder, postorder):
        pos = {}

        for i in range(len(inorder)):
            pos[inorder[i]] = i

        p = [len(postorder) - 1]

        def f(l, r):
            if l > r:
                return None

            x = postorder[p[0]]
            p[0] -= 1

            root = TreeNode(x)
            i = pos[x]

            root.right = f(i + 1, r)
            root.left = f(l, i - 1)

            return root

        return f(0, len(inorder) - 1)