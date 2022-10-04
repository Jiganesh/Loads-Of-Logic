// https://leetcode.com/problems/check-if-matrix-is-x-matrix
// Runtime: 108 ms, faster than 50.69% of JavaScript online submissions for Check if Matrix Is X-Matrix.
// Memory Usage: 45 MB, less than 17.81% of JavaScript online submissions for Check if Matrix Is X-Matrix.
/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var checkXMatrix = function (grid) {
    const n = grid.length;
    let ans = true
    grid.forEach((row, rowIndex) => {
        row.forEach((val, colIndex) => {
            if (rowIndex === colIndex || rowIndex === n - 1 - colIndex) {
                if (val === 0) {
                    ans = false;
                    return;
                }
            } else {
                if (val !== 0) {
                    ans = false;
                    return;
                }
            }
        });
    });
    return ans;
};

module.exports = checkXMatrix;