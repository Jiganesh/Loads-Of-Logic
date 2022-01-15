package greedy;

import java.util.Arrays;

public class nonOverlappingIntervals {
    public static void main(String[] args) {

        SolutionNOI solution = new SolutionNOI();
        System.out.println(solution.eraseOverlapIntervals(new int[][]{{1,2},{2,3},{3,4},{1,3}}));
        
    }   
}

class SolutionNOI {

    // Runtime: 45 ms, faster than 95.96% of Java online submissions for Non-overlapping Intervals.
    // Memory Usage: 96.3 MB, less than 73.77% of Java online submissions for Non-overlapping Intervals.

    // TC : O(NlogN)
    // SC : O(1)
    public int eraseOverlapIntervals(int[][] intervals) {

        Arrays.sort(intervals, (a,b)-> (Integer.compare(a[1], b[1])));
        
        //for (int[]i : intervals ) System.out.println(Arrays.toString(i));

        int prev = intervals[0][1];
        int count  =0;
        for (int i =1 ; i< intervals.length; i++){
            if (intervals[i][0]<prev){
                count ++;
            }else{
                prev = intervals[i][1];
            }
        }
        return count;
    }

    /*
    
    Explanation :

    array = [[1,2],[2,3],[3,4],[1,3]]

    sorting the array wrt last ele in [start, end] so we can get exact idea of the interval
    array = [1,2] [2,3] [1,3] [3,4]

    1   2
        2   3
    1       3
            3   4

    Now we run through all the intervals here 
    obviously if any start of interval is less than the previous intervals the it will be overlapping 
    as you can see in above digram that 1 is less than 3 so it must be overlapping
    hence we increment count

    if the interval is not overlappign we change our previous and assign it to latest interval end value
    */
}