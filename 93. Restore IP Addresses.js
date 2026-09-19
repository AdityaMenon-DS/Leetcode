var restoreIpAddresses = function(s) {
    let ans = [];

    function f(i, a) {
        if (a.length === 4) {
            if (i === s.length) {
                ans.push(a.join("."));
            }
            return;
        }

        for (let j = 1; j <= 3; j++) {
            if (i + j > s.length) {
                break;
            }

            let x = s.substring(i, i + j);

            if (x.length > 1 && x[0] === '0') {
                continue;
            }

            if (Number(x) > 255) {
                continue;
            }

            a.push(x);
            f(i + j, a);
            a.pop();
        }
    }

    f(0, []);

    return ans;
};