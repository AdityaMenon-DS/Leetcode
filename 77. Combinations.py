class Solution(object):
    def combine(self, n, k):
        ans = []

        def f(start, a):
            if len(a) == k:
                ans.append(a[:])
                return

            for i in range(start, n + 1):
                a.append(i)
                f(i + 1, a)
                a.pop()

        f(1, [])

        return ans