class Solution(object):
    def isSymmetric(self, root):
        def mirror(left, right):

            # Both are empty -> symmetric
            if left is None and right is None:
                return True

            # Only one is empty -> not symmetric
            if left is None or right is None:
                return False

            # Values must match
            if left.val != right.val:
                return False

            # Compare opposite children
            return (mirror(left.left, right.right) and
                    mirror(left.right, right.left))

        return mirror(root.left, root.right)