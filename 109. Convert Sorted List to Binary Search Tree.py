class Solution(object):
    def sortedListToBST(self, head):
        a = []

        while head:
            a.append(head.val)
            head = head.next

        def f(l, r):
            if l > r:
                return None

            m = (l + r) // 2

            root = TreeNode(a[m])
            root.left = f(l, m - 1)
            root.right = f(m + 1, r)

            return root

        return f(0, len(a) - 1)