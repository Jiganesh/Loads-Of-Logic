// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

package arrays;

public class minimumSwapsToGroupALL1sTogether {
    public static void main(String[] args) {

        SolutionMSTGA1T solution = new SolutionMSTGA1T();
        System.out.println(solution.minSwaps(new int[]{1,0,1,0,1})); //1
        System.out.println(solution.minSwaps(new int[]{0,1,1,1,0,0,1,1,0}));//2
        System.out.println(solution.minSwaps(new int[]{0,1,0,1,1,0,0})); //1
        System.out.println(solution.minSwaps(new int[]{1,1,0,0,1}));//0
        System.out.println(solution.minSwaps(new int[]{0,0,0}));//0


        
    }
}

class SolutionMSTGA1T{
    public int minSwaps(int[] nums) {
        int n = nums.length;
        int countOne=0 ;
        for (int i : nums) if(i==1) countOne++;
        // countOne represent the length of our sliding window

        int slidingWindowZeroCount =0;
        int minswaps =Integer.MAX_VALUE;

        // slidingWindowZeroCount represents number of zeros present in first window
        // This count will be useful when traversing through array

        for (int i=0; i<countOne; i++) if(nums[i]==0) slidingWindowZeroCount++;

        // While traversing we will check if next element is zero or one and update the minSwaps
        for (int start =0 ; start<n; start++){
            int end = start+countOne;
            end = (end>=n) ? end-n: end;
            slidingWindowZeroCount += (nums[start]==1) ? 0:-1;
            slidingWindowZeroCount += (nums[end]==0) ? 1: 0;
            minswaps = Math.min(slidingWindowZeroCount, minswaps);
        }
        return minswaps ;


        /*
        Example

        {1 0 1 0 1}
        count one = 3  This will be length of sliding window
        the we count how many zeros are present in first sliding window
        we used first for loop for that

        0           1           2   
        1           0           1

        In second for loop we count how many zero are present in window
        obviously that will be the number of swaps we can make
        zeroInWindow = 1
        
        In third for loop we just check and update the count of zero in window
                                    start       end        zeroInWindow                            
        1   0   1 first window      0           3           1
        0   1   0 second window     1           4           2
        1   0   1 third window      2           5-5=0       1
        0   1   1 fourth window     3           6-5=1       1
        1   1   0 fifth window      4           7-5=2       1

        When we update our start we check if the start was zero or not 
        If it is zero we substract if not the we do nothing

        When we update our end we check if the end was zero or not 
        If it was zere then we add to count else we do nothing

        and ofc finally we check that if the swaps required were minimum or not
        */
        
    }
}