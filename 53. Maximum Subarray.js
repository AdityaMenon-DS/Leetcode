var maxSubArray = function(nums) {
    let s = nums[0];
    let ans = nums[0];

    for (let i = 1; i < nums.length; i++) {
        s = Math.max(nums[i], s + nums[i]);
        ans = Math.max(ans, s);
    }

    return ans;
};