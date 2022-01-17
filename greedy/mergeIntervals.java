// https://leetcode.com/problems/merge-intervals/
// Solution : # Solution : https://www.youtube.com/watch?v=2JzRBPFYbKE&t=428s

package greedy;

import java.util.ArrayList;
import java.util.Arrays;

public class mergeIntervals {
    public static void main(String[] args) {

        SolutionMI solution = new SolutionMI();
        print(solution.merge(new int[][]{{1, 3}, {2, 6}, {8, 10}, {15, 18}}));
        print(solution.merge(new int[][]{{1, 4}, {4, 5}}));
        print(solution.merge(new int[][]{{1, 4}, {0, 4},{2,3}}));
        print(solution.merge(new int[][]{{1, 4}, {0, 2}, {3, 5}}));
        print(solution.merge(new int[][]{{2,2},{3,3},{1,3},{5,7},{2,2},{4,6}}));
    
    }
    public static void print(int[][] array){
        for (int[] i : array) System.out.print(Arrays.toString(i)+" ");
        System.out.println();
    }    
}

class SolutionMI {

    // TC : O(N)
    // SC : O(N)
    public int[][] merge(int[][] intervals) {
    
        Arrays.sort(intervals, (a,b)-> Integer.compare(a[0], b[0]));
        ArrayList<int[]> list = new ArrayList<int[]>();
        int[] temp = new int[2];

        temp = intervals[0];
        for (int[] interval : intervals){

            if (temp[1]>= interval[0]){
                temp[1]= Math.max(temp[1], interval[1]);
            }else{
                list.add(temp);
                temp  = interval;
            }
        }
        list.add(temp);
        return list.toArray(new int[list.size()][]);
    }
}