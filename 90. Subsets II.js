var subsetsWithDup = function(nums) {
    nums.sort((a, b) => a - b);

    let ans = [];

    function f(i, a) {
        ans.push([...a]);

        for (let j = i; j < nums.length; j++) {
            if (j > i && nums[j] === nums[j - 1]) {
                continue;
            }

            a.push(nums[j]);
            f(j + 1, a);
            a.pop();
        }
    }

    f(0, []);

    return ans;
};