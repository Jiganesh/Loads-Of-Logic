//https://leetcode.com/problems/two-sum/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
  const sumArr = [];
  nums.forEach((num, index) => {
    const diff = target - num;
    const diffIndex = nums.indexOf(diff);
    if (diffIndex !== -1 && diffIndex !== index) {
      sumArr.push(index, diffIndex);
    }
  });
  return [...new Set(sumArr)].sort();
}
module.exports = twoSum;
