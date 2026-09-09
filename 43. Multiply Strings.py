class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        a = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                x = ord(num1[i]) - ord('0')
                y = ord(num2[j]) - ord('0')

                p = x * y + a[i + j + 1]

                a[i + j + 1] = p % 10
                a[i + j] += p // 10

        i = 0

        while i < len(a) and a[i] == 0:
            i += 1

        return "".join(str(x) for x in a[i:])