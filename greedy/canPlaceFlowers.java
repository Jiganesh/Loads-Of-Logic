package greedy;
// https://leetcode.com/problems/can-place-flowers/


public class canPlaceFlowers {
    public static void main(String[] args) {
        SolutionCPF solution = new SolutionCPF ();
        System.out.println(solution.canPlaceFlowers(new int[]{1,0,0,0,1}, 2));
    }
}

class SolutionCPF {

    // Submitted by @ Jiganesh

    // TC : O(N)
    // SC : O(1)

    // Runtime: 2 ms, faster than 31.85% of Java online submissions for Can Place Flowers.
    // Memory Usage: 49 MB, less than 36.91% of Java online submissions for Can Place Flowers.


    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int len = flowerbed.length;
        for (int i = 0 ; i< len && n>0; i++){
            if (flowerbed[i]==0){
                int prev = (i==0 ||flowerbed[i-1]==0 )?0: 1;
                int next = (i==len-1 || flowerbed[i+1]==0)?0:1;
                
                if (prev==0 && next==0){
                    flowerbed[i]=1;
                    n--;
                }
            }
        }
        return n==0;
    }
}