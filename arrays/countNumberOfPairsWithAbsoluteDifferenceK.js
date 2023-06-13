// Runtime: 95 ms, faster than 73.30% of JavaScript online submissions for Count Number of Pairs With Absolute Difference K.
// Memory Usage: 49.7 MB, less than 5.21% of JavaScript online submissions for Count Number of Pairs With Absolute Difference K.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const countKDifference = (nums, k) => {
    const acc = [];
    for (let i = 0; i < nums.length; i++) {
        helper(k, nums, nums[i], i, acc)
    }
    return acc.length / 2;
};
const helper = (target, arr, val, index, acc) => {
    for (const value of arr) {
        if (Math.abs(val - value) === target) {
            acc.push([val, value])
        }
    }
}
module.exports = countKDifference;