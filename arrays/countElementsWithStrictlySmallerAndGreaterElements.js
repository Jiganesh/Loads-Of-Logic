// Runtime: 68 ms, faster than 85.71% of JavaScript online submissions for Count Elements With Strictly Smaller and Greater Elements .
// Memory Usage: 43.9 MB, less than 24.85% of JavaScript online submissions for Count Elements With Strictly Smaller and Greater Elements .


/**
 * @param {number[]} nums
 * @return {number}
 */
const countElements =  (nums) => {
    let acc = [];
    for (const value of nums) {
        acc.push(helper(nums, value))
    }
    return acc.filter(val => val === true).length;
};
const helper = (arr, val) => {
    let greater = 0;
    let lesser = 0;
    for (const value of arr) {
        if (val > value) {
            greater++;
        }
        if (val < value) {
            lesser++
        }
    }
    return greater > 0 && lesser > 0;
}