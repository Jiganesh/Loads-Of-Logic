// https://leetcode.com/problems/move-zeroes/


// Runtime: 8 ms ms, faster than 99.99% of Python3 online submissions for Move Zeroes.
// Memory Usage: 19.3 MB, less than 57.43% of Python3 online submissions for Move Zeroes.
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int non_zero = 0;
        for(int i =0;i<nums.size();i++)
        {
            if(nums[i]!=0)
                 nums[non_zero++]=nums[i];
        }
        for(int i = non_zero;i<nums.size();i++)
            nums[i]=0;
    }
};
