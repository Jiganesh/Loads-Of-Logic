// https://leetcode.com/problems/build-array-from-permutation/
// Runtime: 248 ms, faster than 5.09% of JavaScript online submissions for Build Array from Permutation.
// Memory Usage: 48.1 MB, less than 6.00% of JavaScript online submissions for Build Array from Permutation.

/**
 * @param {number[]} nums
 * @return {number[]}
 */

var buildArray = function (nums) {
    return nums.reduce((acc, val) => acc.concat(nums[val]), []);
};

module.exports = buildArray;