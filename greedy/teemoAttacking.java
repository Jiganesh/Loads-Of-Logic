package greedy;

//https://leetcode.com/problems/teemo-attacking/

public class teemoAttacking {

    public static void main(String[] args) {

        SolutionTA solution = new SolutionTA();
        System.out.println(solution.findPoisonedDuration(new int[]{1,5,7,8}, 4));
    }
    
}

class SolutionTA {

    // Submitted by @Jiganesh

    // TC : O(N)
    // SC : O(1)

    // Runtime: 2 ms, faster than 61.55% of Java online submissions for Teemo Attacking.
    // Memory Usage: 41.3 MB, less than 48.46% of Java online submissions for Teemo Attacking.

    public int findPoisonedDuration(int[] timeSeries, int duration) {
        
        
        int totalTime = 0;
        int n = timeSeries.length;
        
        for (int i =0 ; i< n ; i++){
            if ((i != n-1) && (timeSeries[i]+duration-1>= timeSeries[i+1])){
                totalTime+=timeSeries[i+1]-timeSeries[i];
            }
            else{
                 totalTime += duration;
            }
        }             
        return totalTime;    
    }

    /*
    Example
    
    timeSeries = [1,5,7,8]  duration = 4
    
    poisonEffect remains from [t , t+ duration-1] (inclusive)
    
    poisonEffect Duration
    [1-4]  poison effect = 4
    [5-8]  poison effect 5 to 8 but after attack of 7 it will reset so it will be [5-7] poison effect = 2
            (5,6) because on 7 there will be next attack and this will be added in next part
    [7-10] poison effect 7 to 10 but after attack of 8 it will reset so it will be [7-8] poison effect =1
            (7) because on 8 there will be next attack and this will be added in next part
    [8-11] last element in timeSeries so it will have full duration poison effect = 4
    
    Hence Answer will be 11

    */
}