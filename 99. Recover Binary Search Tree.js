var recoverTree = function(root) {
    let first = null;
    let second = null;
    let prev = null;
    let cur = root;

    while (cur !== null) {
        if (cur.left === null) {
            if (prev !== null && prev.val > cur.val) {
                if (first === null) {
                    first = prev;
                }
                second = cur;
            }

            prev = cur;
            cur = cur.right;
        } else {
            let p = cur.left;

            while (p.right !== null && p.right !== cur) {
                p = p.right;
            }

            if (p.right === null) {
                p.right = cur;
                cur = cur.left;
            } else {
                p.right = null;

                if (prev !== null && prev.val > cur.val) {
                    if (first === null) {
                        first = prev;
                    }
                    second = cur;
                }

                prev = cur;
                cur = cur.right;
            }
        }
    }

    let x = first.val;
    first.val = second.val;
    second.val = x;
};