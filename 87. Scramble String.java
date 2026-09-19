import java.util.*;

class Solution {
    HashMap<String, Boolean> m = new HashMap<>();

    public boolean isScramble(String s1, String s2) {
        if (s1.equals(s2)) {
            return true;
        }

        String key = s1 + "#" + s2;

        if (m.containsKey(key)) {
            return m.get(key);
        }

        if (s1.length() != s2.length()) {
            return false;
        }

        int[] a = new int[26];

        for (int i = 0; i < s1.length(); i++) {
            a[s1.charAt(i) - 'a']++;
            a[s2.charAt(i) - 'a']--;
        }

        for (int x : a) {
            if (x != 0) {
                m.put(key, false);
                return false;
            }
        }

        int n = s1.length();

        for (int i = 1; i < n; i++) {

            boolean noSwap =
                isScramble(s1.substring(0, i), s2.substring(0, i)) &&
                isScramble(s1.substring(i), s2.substring(i));

            if (noSwap) {
                m.put(key, true);
                return true;
            }

            boolean swap =
                isScramble(s1.substring(0, i), s2.substring(n - i)) &&
                isScramble(s1.substring(i), s2.substring(0, n - i));

            if (swap) {
                m.put(key, true);
                return true;
            }
        }

        m.put(key, false);
        return false;
    }
}