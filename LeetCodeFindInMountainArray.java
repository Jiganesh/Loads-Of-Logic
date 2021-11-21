/**
 * This is MountainArray's API interface.
 * You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */

 /*
class Solution {
    
    public int findInMountainArray(int target, MountainArray mountainArr) {
        if (mountainArr.length() >1){
            int peakIndex = peakInArray (mountainArr);

            int left = orderAgnosticBinarySearch (mountainArr, target, 0, peakIndex);
            if (left >-1) return left;
            int right = orderAgnosticBinarySearch(mountainArr, target , peakIndex+1, mountainArr.length()-1);
            if(right >-1) return right;
            else return -1;
        }
        return -1;
    }
    
    public int orderAgnosticBinarySearch(MountainArray array, int target, int start , int end){
        boolean isAsc = array.get(start)<array.get(end);
        while(start <= end){
            int mid = start +(end -start)/2;
            int midelement = array.get(mid);
            if (midelement==target) return mid;
            if (isAsc){
                if (midelement<target){
                    start = mid+1;
                }else if (midelement>target){
                    end = mid-1;
                }
            }else{
                if (midelement<target){
                    end = mid -1;
                }else if(midelement>target){
                    start = mid+1;
                }
            }
        }
        return -1;
    }
    public int peakInArray (MountainArray mountainArr){
        int start = 0;
        int end = mountainArr.length()-1;
        while(start != end ){
            int mid = start + (end -start)/2;
            if(mountainArr.get(mid)< mountainArr.get(mid+1)) start = mid +1;
            else if (mountainArr.get(mid)> mountainArr.get(mid+1) )end = mid;
        }
        return start;
    }
}

*/

//Leetcode Solution for Find In Mountain Array
// Concept is explained in FindInMountainArray.java file
