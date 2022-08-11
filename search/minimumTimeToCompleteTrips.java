package search ; 

public class minimumTimeToCompleteTrips{
    public static void main(String[] args) {

        SolutionMITCT solution = new SolutionMITCT();
        System.out.println(solution.minimumTime(new int[]{1,2,3}, 5));
        
    }
}

class SolutionMITCT {

    // TC: O(N log P) N is No of buses where P is end
    // SC : O(1);

    public long minimumTime(int[] time, int totalTrips) {

        // Choosing Start and end

        // Use binary search to locate the minimum time, which cost O(nlog(range)), 
        // where n = time.length, range = higher bound - lower bound.
        // Specify search space range:
        // a) lower bound is 0;
        // b) higher bound:
        // According to the ranges in the problem, 1 <= time.length <= 10^5 1 <= time[i], totalTrips <= 10^7.
        // Therefore, the longest time, the higher bound of the binary search space, 10 ^ 7 * 10 ^ 7, 
        // which corresponds to the worst case that only 1 bus is available and it need to finish 10 ^ 7 trips.
        

        
        long start = 0;
        
        // end can be reduced to tighter space by some logice
        // The upper bound has a closed form given by: highestTime = min(time) * totalTrips
        // This is because, in the worst case, we only use the bus which is the fastest to do all the trips.
        
        long minTime = time[0];
        for (int i : time) minTime = Math.min(i, minTime);
        long end = minTime*totalTrips;
        
        
        while (start<=end){
            
            long mid = (end-start)/2+start;            
            long totalTripsDone = 0;
            
            for (int i : time){
                totalTripsDone += mid/i;
            }
        
            if (totalTripsDone >= totalTrips) {
                end = mid-1;
            }else {
                start = mid+1;
            }        
        }
        return start;
        
    }
}