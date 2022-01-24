package binarySearch;

// https://leetcode.com/problems/koko-eating-bananas/
import java.util.Arrays;

public class kokoEatingBananas{
    public static void main(String[] args) {
        SolutionKEB solution = new SolutionKEB();
        System.out.println(solution.minEatingSpeed(new int[]{3,6,7,11}, 8));
        System.out.println(solution.minEatingSpeed(new int[]{30,11,23,4,20}, 5));
        System.out.println(solution.minEatingSpeed(new int[]{30,11,23,4,20}, 6));
        System.out.println(solution.minEatingSpeed(new int[]{312884470},968709470));

    }
}
class SolutionKEB {

    // Submitted by @Jiganesh

    // TC : O(NLogM)
    // SC : O(1)
    public int minEatingSpeed(int[] piles, int h) {
        
        
        int start = 1;
        int end = Arrays.stream(piles).max().getAsInt();
        int eatingspeed = end;
        while(start<=end){
            
            int mid = start +(end-start)/2;
            int hoursTaken = kBananas(mid, piles);

            if( hoursTaken <= h){
                eatingspeed = Math.min(eatingspeed, mid);
                end = mid-1;
            }else {
                start = mid+1;
            } 
        }
        return eatingspeed;
        
        
    }
    
    public int kBananas(int n, int[] array){
        
        int total=0;
        for (int i : array){
            total+=Math.ceil((double)i/ (double)n);
        }
        return total;
    }
}