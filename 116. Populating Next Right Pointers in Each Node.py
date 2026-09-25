class Solution(object):
    def connect(self, root):
        if not root:
            return root

        left = root

        while left.left:
            cur = left

            while cur:
                cur.left.next = cur.right

                if cur.next:
                    cur.right.next = cur.next.left

                cur = cur.next

            left = left.left

        return root