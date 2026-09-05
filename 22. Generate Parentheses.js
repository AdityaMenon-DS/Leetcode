/*
22. Generate Parentheses
Medium
Topics
premium lock icon
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
*/
var generateParenthesis = function(n) {
    let a = [];

    function f(s, o, c) {
        if (s.length === 2 * n) {
            a.push(s);
            return;
        }

        if (o < n) {
            f(s + "(", o + 1, c);
        }

        if (c < o) {
            f(s + ")", o, c + 1);
        }
    }

    f("", 0, 0);

    return a;
};