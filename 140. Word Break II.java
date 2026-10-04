import java.util.*;

class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        Map<Integer, List<String>> memo = new HashMap<>();

        return dfs(s, 0, set, memo);
    }

    private List<String> dfs(String s, int i, Set<String> set,
                             Map<Integer, List<String>> memo) {

        if (memo.containsKey(i)) {
            return memo.get(i);
        }

        List<String> ans = new ArrayList<>();

        if (i == s.length()) {
            ans.add("");
            return ans;
        }

        for (int j = i + 1; j <= s.length(); j++) {
            String word = s.substring(i, j);

            if (set.contains(word)) {
                List<String> rest = dfs(s, j, set, memo);

                for (String x : rest) {
                    if (x.isEmpty()) {
                        ans.add(word);
                    } else {
                        ans.add(word + " " + x);
                    }
                }
            }
        }

        memo.put(i, ans);
        return ans;
    }
}