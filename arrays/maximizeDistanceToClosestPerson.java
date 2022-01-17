package arrays;
// https://leetcode.com/problems/maximize-distance-to-closest-person/
// Solution : https://www.youtube.com/watch?v=Ngf1XUDfK7M4
public class maximizeDistanceToClosestPerson {
    public static void main(String[] args) {

        SolutionMDTCP solution = new SolutionMDTCP();
        System.out.println(solution.maxDistToClosest(new int[]{1,0,0,0,1,0,1}));
        System.out.println(solution.maxDistToClosest(new int[]{0,0,0,0,1,0,1}));
        System.out.println(solution.maxDistToClosest(new int[]{1,0,0,0,0,0}));

        System.out.println(solution.maxDistToClosestApproach2(new int[]{1,0,0,0,1,0,1}));
        System.out.println(solution.maxDistToClosestApproach2(new int[]{0,0,0,0,1,0,1}));
        System.out.println(solution.maxDistToClosestApproach2(new int[]{1,0,0,0,0,0}));   
    }
    
}

class SolutionMDTCP{
    public int maxDistToClosest(int[] seats) {

        int len = seats.length;
        int gap = Integer.MIN_VALUE;
        int lst = 0;
        int fst = 0;
        int ind = 0;
        int steps = 0;

        if (seats[0] == 0) {

            for (int i = 0; i < len; i++) {
                if (seats[i] == 1) {
                    ind = i;
                    fst = steps;
                    break;
                } else
                    steps++;
            }
        }

        steps = 0;
        for (int i = ind; i < len; i++) {

            if (i == len - 1 && seats[i] == 0) {
                lst = steps + 1;
                break;
            }

            if (seats[i] == 0) {
                steps++;
            }
            if (seats[i] == 1) {
                if (steps > gap)
                    gap = steps;
                steps = 0;
            }
        }

        int mid_gap = (int) Math.floor((gap + 1) / (double) 2);

        if (fst >= lst && fst >= mid_gap)
            return fst;
        else if (mid_gap >= fst && mid_gap >= lst)
            return mid_gap;
        else
            return lst;

    }

    // TC: O(N)
    // SC: O(1)

    // Easy and Efficient Solution

    // Runtime: 2 ms, faster than 77.87% of Java online submissions for Maximize Distance to Closest Person.
    // Memory Usage: 46.6 MB, less than 15.31% of Java online submissions for Maximize Distance to Closest Person.
    
    public int maxDistToClosestApproach2(int[] seats) {
        
        int totalSeats = seats.length;
        int firstOccurenceOfOne = -1;
        int countOfZeroesBetweenTwoSeats=0;
        int maximumDistance = 0;
        
        for (int i = 0; i<totalSeats; i++){
            if (seats[i]==0) countOfZeroesBetweenTwoSeats++;
            else if (seats[i]==1){
                if(firstOccurenceOfOne ==-1){
                    maximumDistance = countOfZeroesBetweenTwoSeats;
                    firstOccurenceOfOne =i;
                }else{
                    maximumDistance= Math.max(maximumDistance,(countOfZeroesBetweenTwoSeats+1)/2);
                }
                countOfZeroesBetweenTwoSeats=0;
            }
            
        }
        return Math.max(maximumDistance,countOfZeroesBetweenTwoSeats);
    }
}
