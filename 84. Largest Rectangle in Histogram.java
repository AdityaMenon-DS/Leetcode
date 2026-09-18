import java.util.*;

class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> st = new Stack<>();
        int ans = 0;

        for (int i = 0; i <= heights.length; i++) {
            int h = (i == heights.length) ? 0 : heights[i];

            while (!st.isEmpty() && heights[st.peek()] > h) {
                int x = st.pop();
                int height = heights[x];

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