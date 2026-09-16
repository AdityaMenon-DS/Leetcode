class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = {}
        for x in t:
            need[x] = need.get(x, 0) + 1

        have = {}
        l = 0
        count = 0
        ans = ""
        best = float("inf")

        for r in range(len(s)):
            x = s[r]
            have[x] = have.get(x, 0) + 1

            if x in need and have[x] <= need[x]:
                count += 1

            while count == len(t):
                if r - l + 1 < best:
                    best = r - l + 1
                    ans = s[l:r + 1]

                y = s[l]
                have[y] -= 1

                if y in need and have[y] < need[y]:
                    count -= 1

                l += 1

        return ans