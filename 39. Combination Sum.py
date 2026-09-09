class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []

        def f(i, s, a):
            if s == target:
                ans.append(a[:])
                return

            if s > target or i == len(candidates):
                return

            a.append(candidates[i])
            f(i, s + candidates[i], a)
            a.pop()

            f(i + 1, s, a)

        f(0, 0, [])

        return ans
        