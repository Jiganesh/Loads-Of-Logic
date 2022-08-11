package search;

public class searchInRotatedSortedArrayII {
    public static void main(String[] args) {
        SolutionSISAII solution = new SolutionSISAII();
        System.out.println(solution.search(new int[] { 1, 0, 1, 1, 1 }, 0));
    }

}

class SolutionSISAII {
    public boolean search(int[] nums, int target) {
        int pivot = (findPivot(nums));

        if (pivot == -1)
            return binarySearch(nums, target, 0, nums.length - 1);
        if (target >= nums[0])
            return binarySearch(nums, target, 0, pivot);
        return binarySearch(nums, target, pivot + 1, nums.length - 1);
    }

    public boolean binarySearch(int[] array, int target, int start, int end) {
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (array[mid] > target)
                end = mid - 1;
            else if (array[mid] < target)
                start = mid + 1;
            else
                return true;
        }
        return false;

    }

    public int findPivot(int[] array) {
        int start = 0;
        int end = array.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;
            int midelement = array[mid];
            if (mid > start && array[mid - 1] > midelement)
                return mid - 1;
            if (mid < end && midelement > array[mid + 1])
                return mid;

            if (midelement == array[start] && midelement == array[end]) {
                if (start < end && array[start] > array[start + 1])
                    return start;
                start++;
                if (end > start && array[end - 1] > array[end])
                    return end;
                end--;
            } else if (midelement > array[start] || (array[start] == midelement && midelement > array[end]))
                start = mid + 1;
            else
                end = end - 1;
        }
        return -1;
    }

}
