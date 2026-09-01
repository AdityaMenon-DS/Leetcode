'''
5. Longest Palindromic Substring
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        st=0
        e=0

        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i + 1)

            l=max(len1, len2)

            if l> e-st:
                st= i-(l - 1)//2
                e=i+l//2
        return s[st:e+1]
    def expand(self, s, le, r):
        while le>= 0 and r< len(s) and s[le] == s[r]:
            le-= 1
            r+= 1

        return r-le- 1