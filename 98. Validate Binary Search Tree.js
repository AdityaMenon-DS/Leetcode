var isValidBST = function(root) {
    function f(node, low, high) {
        if (node === null) {
            return true;
        }

        if (node.val <= low || node.val >= high) {
            return false;
        }

        return (
            f(node.left, low, node.val) &&
            f(node.right, node.val, high)
        );
    }

    return f(root, -Infinity, Infinity);
};