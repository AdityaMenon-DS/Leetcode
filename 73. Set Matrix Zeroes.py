class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        row0 = False
        col0 = False

        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True

        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0:
            for j in range(n):
                matrix[0][j] = 0

        if col0:
            for i in range(m):
                matrix[i][0] = 0
                matrix[i][0] = 0