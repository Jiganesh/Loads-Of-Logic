
// Runtime: 84 ms, faster than 61.76% of JavaScript online submissions for Alphabet Board Path.
// Memory Usage: 43.6 MB, less than 26.47% of JavaScript online submissions for Alphabet Board Path.
// /**
//  * @param {string} target
//  * @return {string}
//  */
function alphabetBoardPath(target) {
  const board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"];
  const boardMap = new Map();
  board.forEach((row, rowIndex) => {
    row.split("").forEach((letter, colIndex) => {
      boardMap.set(letter, [rowIndex, colIndex]);
    });
  });
  const targetAttr = target.split("").map((letter) => boardMap.get(letter));
  const result = [];
  let prevAttr = [0, 0];
  targetAttr.forEach((attr) => {
    const [row, col] = attr;
      const [prevRow, prevCol] = prevAttr;
      if (row === 5 && col === 0) {
          if (row > prevRow) {
              result.push("D".repeat(row - prevRow - 1));
          }
          if (col < prevCol) {
              result.push("L".repeat(prevCol - col));
          }
          if (row > prevRow) {
              result.push("D".repeat(1));
          }
      }
      else {
          if (prevRow > row) {
              result.push("U".repeat(prevRow - row));
          }
          if (row > prevRow) {
              result.push("D".repeat(row - prevRow));
          }
          if (col < prevCol) {
              result.push("L".repeat(prevCol - col));
          }
          if (prevCol < col) {
              result.push("R".repeat(col - prevCol));
          }
      }
    result.push("!");
    prevAttr = attr;
  });
  return result.join("");
}
console.log(alphabetBoardPath("zdz"));
module.exports = alphabetBoardPath;
