'''
10. Regular Expression Matching
Hard
Topics
premium lock icon
Companies
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''
class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                first_match = (
                    i < m and
                    (s[i] == p[j] or p[j] == '.')
                )

                if j + 1 < n and p[j + 1] == '*':
                    dp[i][j] = (
                        dp[i][j + 2] or
                        (first_match and dp[i + 1][j])
                    )
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]