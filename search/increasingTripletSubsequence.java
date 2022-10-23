//https://leetcode.com/problems/increasing-triplet-subsequence/

package search;

import java.util.ArrayList;
import java.util.List;

class increasingTripletSubsequence {
     //TC : O(N*log(N))
     //SC : O(N),just to store the increasing subsequence.
     int lower_bound(List<Integer> arr, int key) {
        int low = 0, high = arr.size();
        int mid;
        while (low < high) {
            mid = low + (high - low) / 2;
            if (key <= arr.get(mid)) {
                high = mid;
            } else {

                low = mid + 1;
            }
        }
        if (low < arr.size() && arr.get(low) < key) {
            low++;
        }
        return low;
    }   
    public boolean increasingTriplet(int[] nums) {
        List<Integer> temp = new ArrayList <Integer>();
        temp.add(nums[0]);
        for(int i=1;i<nums.length;i++){
            if(temp.get(temp.size()-1)<nums[i]){
                temp.add(nums[i]);
            }
            else{
                int idx = lower_bound(temp,nums[i]);
                temp.set(idx,nums[i]);
            }
        }
        if(temp.size()>=3) return true;
        return false;
    }
}
