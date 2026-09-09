class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []

        def f(i, s, a):
            if s == target:
                ans.append(a[:])
                return

            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if s + candidates[j] > target:
                    break

                a.append(candidates[j])
                f(j + 1, s + candidates[j], a)
                a.pop()

        f(0, 0, [])

        return ans