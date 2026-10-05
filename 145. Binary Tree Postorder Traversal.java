import java.util.*;

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();

        if (root == null) {
            return ans;
        }

        Stack<TreeNode> st = new Stack<>();
        st.push(root);

        while (!st.isEmpty()) {
            TreeNode node = st.pop();

            ans.add(node.val);

            if (node.left != null) {
                st.push(node.left);
            }

            if (node.right != null) {
                st.push(node.right);
            }
        }

        Collections.reverse(ans);

        return ans;
    }
}