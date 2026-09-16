class Solution(object):
    def subsets(self, nums):
        ans = []

        def f(i, a):
            if i == len(nums):
                ans.append(a[:])
                return

            f(i + 1, a)

            a.append(nums[i])
            f(i + 1, a)
            a.pop()

        f(0, [])

        return ans