var totalNQueens = function(n) {
    let ans = 0;

    let col = new Set();
    let d1 = new Set();
    let d2 = new Set();

    function f(r) {
        if (r === n) {
            ans++;
            return;
        }

        for (let c = 0; c < n; c++) {
            if (col.has(c) || d1.has(r - c) || d2.has(r + c)) {
                continue;
            }

            col.add(c);
            d1.add(r - c);
            d2.add(r + c);

            f(r + 1);

            col.delete(c);
            d1.delete(r - c);
            d2.delete(r + c);
        }
    }

    f(0);

    return ans;
};