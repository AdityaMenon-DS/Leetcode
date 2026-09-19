import java.util.*;

class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) {
            return 0;
        }

        int n = matrix[0].length;
        int[] h = new int[n];
        int ans = 0;

        for (int i = 0; i < matrix.length; i++) {

            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    h[j]++;
                } else {
                    h[j] = 0;
                }
            }

            ans = Math.max(ans, area(h));
        }

        return ans;
    }

    public int area(int[] h) {
        Stack<Integer> st = new Stack<>();
        int ans = 0;

        for (int i = 0; i <= h.length; i++) {
            int x = (i == h.length) ? 0 : h[i];

            while (!st.isEmpty() && h[st.peek()] > x) {
                int p = st.pop();
                int height = h[p];

                int width;

                if (st.isEmpty()) {
                    width = i;
                } else {
                    width = i - st.peek() - 1;
                }

                ans = Math.max(ans, height * width);
            }

            st.push(i);
        }

        return ans;
    }
}