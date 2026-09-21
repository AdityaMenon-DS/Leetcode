var generateTrees = function(n) {
    function f(l, r) {
        let a = [];

        if (l > r) {
            a.push(null);
            return a;
        }

        for (let i = l; i <= r; i++) {
            let left = f(l, i - 1);
            let right = f(i + 1, r);

            for (let x of left) {
                for (let y of right) {
                    let root = new TreeNode(i);
                    root.left = x;
                    root.right = y;

                    a.push(root);
                }
            }
        }

        return a;
    }

    return f(1, n);
};