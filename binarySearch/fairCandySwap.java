package binarySearch;

import java.util.Arrays;

// https://leetcode.com/problems/fair-candy-swap/

public class fairCandySwap {
    public static void main(String[] args) {
        
    }
}

class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        int totalAlice = total(aliceSizes);
        int totalBob = total (bobSizes);

        // totalAliceCandy-AliceExchangeCandy = totalBobCandy-BobExchangeCandy
        // difference of Candies Alice and Bob = (totalAliceCandy-totalBobCandy ) /2
        // (totalAliceCandy-totalBobCandy ) /2 + BobExchangeCandy = AliceExchangeCandy
        int difference = (totalAlice-totalBob)/2;

        // so we need to see if alice has the candy which he can exchange with bob
        // We will apply sort so that we can apply binary Search on it
        // We keep space Complexity to O(1) sacrificing  efficiency in Time Complexity to Sort
        // If Space complexity is not issue you can use HashSet to search

        Arrays.sort(aliceSizes); // N log N
        for(int i : bobSizes){
            if(binarySearch(aliceSizes,difference+i) >=0 ) return new int[]{difference+i, i};
        }
        return null;
    }
    // With binary Search approach you get slightly higher time but u save some extra space; (14 ms)
    // With HashSet Seaching becomes O(1) so TC is lesser (9 ms) This will be most efficient solution for this case;

    public int binarySearch(int[] array, int target){
        int start = 0;
        int end = array.length-1;

        while(start <=end){
            int mid = start + (end -start)/2;
            if (array[mid]<target) start = mid+1;
            else if (array[mid]>target) end = mid-1;
            else return mid;
        }
        return -1;
    }

    public int total(int [] array){
        int total = 0;
        for (int i : array){
            total +=i;
        }
        return total;
    }
}
