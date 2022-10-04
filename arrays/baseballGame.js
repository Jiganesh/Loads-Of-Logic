// https://leetcode.com/problems/baseball-game/
// Runtime: 94 ms, faster than 58.80% of JavaScript online submissions for Baseball Game.
// Memory Usage: 47.6 MB, less than 7.14% of JavaScript online submissions for Baseball Game.
/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function (operations) {
  let solution = [];
  operations.forEach((val) => {
    if (!!Number(val)) {
      solution.push(Number(val));
    } else if (val === "C") {
      solution.pop();
    } else if (val === "D") {
      solution = [...solution, solution[solution.length - 1] * 2];
    } else if (val === "+") {
      solution = [
        ...solution,
        solution[solution.length - 1] + solution[solution.length - 2],
      ];
    }
  });
  return solution.reduce((acc, cur) => acc + cur, 0);
};
module.exports = calPoints;
