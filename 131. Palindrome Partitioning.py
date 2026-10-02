class Solution(object):
    def partition(self, s):
        ans = []
        path = []

        def isPal(x):
            return x == x[::-1]

        def f(i):
            if i == len(s):
                ans.append(path[:])
                return

            for j in range(i, len(s)):
                x = s[i:j + 1]

                if isPal(x):
                    path.append(x)
                    f(j + 1)
                    path.pop()

        f(0)
        return ans