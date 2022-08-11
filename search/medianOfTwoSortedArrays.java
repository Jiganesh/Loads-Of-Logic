package search;

// https://leetcode.com/problems/median-of-two-sorted-arrays

public class medianOfTwoSortedArrays {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merged = new int[nums1.length + nums2.length];
        int startnums1 = 0, startnums2 = 0, i = 0;
        while (startnums1 < nums1.length && startnums2 < nums2.length) {
            if (nums1[startnums1] < nums2[startnums2])
                merged[i++] = nums1[startnums1++];
            else
                merged[i++] = nums2[startnums2++];
        }
        while (startnums1 < nums1.length)
            merged[i++] = nums1[startnums1++];
        while (startnums2 < nums2.length)
            merged[i++] = nums2[startnums2++];
        double median = 0;
        int mid = merged.length / 2;
        if (merged.length % 2 == 0)
            median = (double) (merged[mid] + merged[mid - 1]) / 2;
        else
            median = (double) merged[mid];
        return median;
    }
}
