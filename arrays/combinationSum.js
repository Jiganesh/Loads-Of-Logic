/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
let can, n;
const combinationSum = (a, target) => {
    a.sort((x, y) => x - y);
    let res = [];
    can = a; n = a.length;
    helper(target, 0, res, []);
    return res;
};

const helper = (sum, start, res, path) => {
    if (sum == 0) return res.push([...path]);
    for (let i = start; i < n; i++) {
        if (can[i] > sum) return;
        path.push(can[i]);
        helper(sum - can[i], i, res, path); // allow select the same number, change i + 1 to i 
        path.pop();
    }
};
module.exports = combinationSum;