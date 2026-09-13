var merge = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);

    let ans = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        let last = ans[ans.length - 1];

        if (intervals[i][0] <= last[1]) {
            last[1] = Math.max(last[1], intervals[i][1]);
        } else {
            ans.push(intervals[i]);
        }
    }

    return ans;
};