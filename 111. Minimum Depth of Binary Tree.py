from collections import deque

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            node, d = q.popleft()

            if not node.left and not node.right:
                return d

            if node.left:
                q.append((node.left, d + 1))

            if node.right:
                q.append((node.right, d + 1))