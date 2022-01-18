package greedy;

// https://leetcode.com/problems/remove-covered-intervals/


import java.util.Arrays;
public class removeCoveredIntervals {
    public static void main(String[] args) {
    
        SolutionRCI solution= new SolutionRCI ();
        System.out.println(solution.removeCoveredIntervals(new int [][]{{1,2},{1,4},{3,8}}));  
    }
}

class SolutionRCI {

    // Submitted by @ Jiganesh
    // TC : O(NlogN)
    // SC : O(1)

    // Runtime: 5 ms, faster than 66.26% of Java online submissions for Remove Covered Intervals.
    // Memory Usage: 39.3 MB, less than 70.35% of Java online submissions for Remove Covered Intervals.

    public int removeCoveredIntervals(int[][] intervals) {
        
        int count =intervals.length;
        Arrays.sort(intervals, (a,b)-> Integer.compare(a[0],b[0]));
        
        int c = intervals[0][0];
        int d = intervals [0][1];
        
        for (int i =1 ; i< intervals.length ;i++){
            int a = intervals[i][0];
            int b = intervals[i][1];
            if ((c<=a  && b<=d)|| (a<=c && d<=b)) {
                count--;
                d = (b>d)?b:d;
            }
            else {
                c=a;
                d=b;
            }
        }
        return count;   
    }
}