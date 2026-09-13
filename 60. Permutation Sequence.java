import java.util.*;

class Solution {
    public String getPermutation(int n, int k) {
        List<Integer> a = new ArrayList<>();

        int f = 1;

        for (int i = 1; i <= n; i++) {
            a.add(i);

            if (i < n) {
                f *= i;
            }
        }

        k--;

        String ans = "";

        while (!a.isEmpty()) {
            int i = k / f;

            ans += a.get(i);
            a.remove(i);

            k = k % f;

            if (!a.isEmpty()) {
                f = f / a.size();
            }
        }

        return ans;
    }
}