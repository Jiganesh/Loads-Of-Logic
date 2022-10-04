// https://leetcode.com/problems/build-array-from-permutation/
/**
 * @param {number[]} nums
 * @return {number[]}
 */

var buildArray = function (nums) {
    return nums.reduce((acc, val) => acc.concat(nums[val]), []);
};

module.exports = buildArray;