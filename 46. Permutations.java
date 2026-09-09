import java.util.*;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        boolean[] used = new boolean[nums.length];

        f(nums, new ArrayList<>(), used, ans);

        return ans;
    }

    void f(int[] nums, List<Integer> a, boolean[] used, List<List<Integer>> ans) {
        if (a.size() == nums.length) {
            ans.add(new ArrayList<>(a));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }

            used[i] = true;
            a.add(nums[i]);

            f(nums, a, used, ans);

            a.remove(a.size() - 1);
            used[i] = false;
        }
    }
}