var inorderTraversal = function(root) {
    let ans = [];
    let st = [];
    let p = root;

    while (p !== null || st.length > 0) {

        while (p !== null) {
            st.push(p);
            p = p.left;
        }

        p = st.pop();
        ans.push(p.val);

        p = p.right;
    }

    return ans;
};