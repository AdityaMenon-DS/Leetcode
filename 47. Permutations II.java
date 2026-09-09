import java.util.*;

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();

        Arrays.sort(nums);

        boolean[] used = new boolean[nums.length];

        f(nums, used, new ArrayList<>(), ans);

        return ans;
    }

    void f(int[] nums, boolean[] used, List<Integer> a, List<List<Integer>> ans) {
        if (a.size() == nums.length) {
            ans.add(new ArrayList<>(a));
            return;
        }

        for (int i = 0; i < nums.length; i++) {

            if (used[i]) {
                continue;
            }

            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }

            used[i] = true;
            a.add(nums[i]);

            f(nums, used, a, ans);

            a.remove(a.size() - 1);
            used[i] = false;
        }
    }
}