package bitManipulation;

/*
Time complexity:O(n)
Space Complexity:O(1)
*/
class missingNumberInArray {

    public int missingNumber(int[] nums) {

		int xor = 0, i = 0;
		for (i = 0; i < nums.length; i++) {
			xor = xor ^ i ^ nums[i];
		}

		return xor ^ i;
	}
}
