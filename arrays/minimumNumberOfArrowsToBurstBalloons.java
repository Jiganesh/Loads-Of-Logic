package arrays;

import java.util.Arrays;

// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

public class minimumNumberOfArrowsToBurstBalloons {
    public static void main(String[] args) {

        SolutionMNOATBB solution = new SolutionMNOATBB();
        System.out.println(solution.findMinArrowShots(new int[][] { { 9, 12 }, { 1, 10 }, { 4, 11 }, { 8, 12 }, { 3, 9 }, { 6, 9 }, { 6, 7 } }));

    }
}

class SolutionMNOATBB {

    // TC : O(N)
    // SC : O(1)
    public int findMinArrowShots(int[][] points) {

        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        // for(int[] point : points) System.out.println(Arrays.toString(point));
        int prev = points[0][1];
        int count = 0;

        for (int[] point : points) {
            if (prev < point[0]) {
                count++;
                prev = point[1];
            }
        }

        return count + 1;

    }
}