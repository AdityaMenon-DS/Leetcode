from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            a = []

            for i in range(len(q)):
                x = q.popleft()
                a.append(x.val)

                if x.left:
                    q.append(x.left)

                if x.right:
                    q.append(x.right)

            ans.append(a)

        return ans[::-1]