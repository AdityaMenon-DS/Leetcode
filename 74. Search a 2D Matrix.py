class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2

            i = mid // n
            j = mid % n

            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False