package arrays;

/* https://leetcode.com/problems/get-the-maximum-score */

public class getTheMaxScore {

    /* Two Pointer Approach */
    public int maxSum(int[] nums1, int[] nums2) {
        // initializing two pointer vars
        int i = 0, j = 0;
        int len1 = nums1.length, len2 = nums2.length;

        // taking the vars of long type to avoid integer overflow or runtime error
        long upperSum = 0, lowerSum = 0;

        // traverse till one of the arrays length
        while (i < len1 && j < len2) {

            // adding the element to the upperSum until element of first array is >=
            // the element of second array & then increamenting the pointer var by 1
            if (nums1[i] < nums2[j])
                upperSum += nums1[i++];

            // adding the element to the lowerSum until element of second array is >=
            // the element of first array & then increamenting the pointer var by 1
            else if (nums1[i] > nums2[j])
                lowerSum += nums2[j++];

            // when the element of both arrays are equal,
            // assign the value of max of upperSum & lowerSum and adding the element itself
            else {
                upperSum = lowerSum = Math.max(upperSum, lowerSum) + nums1[i];
                // increasing both pointer by 1, as the value at both the pointers is same,
                // avoiding the repetition of element in the sum
                i++;
                j++;
            }
        }

        // adding the remaining element from first array
        while (i < len1)
            upperSum += nums1[i++];

        // adding the remaining element from second array
        while (j < len2)
            lowerSum += nums2[j++];

        return (int) (Math.max(upperSum, lowerSum) % 1000000007);
    }
}
