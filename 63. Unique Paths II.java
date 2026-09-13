class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        int[][] a = new int[m][n];

        if (obstacleGrid[0][0] == 1) {
            return 0;
        }

        a[0][0] = 1;

        for (int i = 1; i < m; i++) {
            if (obstacleGrid[i][0] == 0) {
                a[i][0] = a[i - 1][0];
            }
        }

        for (int j = 1; j < n; j++) {
            if (obstacleGrid[0][j] == 0) {
                a[0][j] = a[0][j - 1];
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 0) {
                    a[i][j] = a[i - 1][j] + a[i][j - 1];
                }
            }
        }

        return a[m - 1][n - 1];
    }
}