// Runtime: 123 ms, faster than 92.56% of JavaScript online submissions for Check if Every Row and Column Contains All Numbers.
// Memory Usage: 50.3 MB, less than 65.29% of JavaScript online submissions for Check if Every Row and Column Contains All Numbers.
// Next challenges:
/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var checkValid = function (matrix) {
  const matrixLength = matrix.length;
  // search rows
  for (var i = 0; i < matrixLength; i++) {
    var solutionSet = new Set();
    for (var j = 0; j < matrixLength; j++) {
      if (solutionSet.has(matrix[i][j])) {
        return false;
      } else {
        solutionSet.add(matrix[i][j]);
      }
    }
  }
  // search columns
  for (var i = 0; i < matrixLength; i++) {
    var solutionSet = new Set();
    for (var j = 0; j < matrixLength; j++) {
      if (solutionSet.has(matrix[j][i])) {
        return false;
      } else {
        solutionSet.add(matrix[j][i]);
      }
    }
  }
  return true;
};
module.exports = checkValid;
