/**
 * @param {number[][]} mat
 * @return {number[]}
 */
const findDiagonalOrder = (mat) => {
    let rows = mat.length;
    let cols = mat[0].length;
    let result = new Array(rows + cols - 1).fill(null).map(() => []);

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if ((row + col) % 2 === 0) result[row + col].unshift(mat[row][col]);
            else result[row + col].push(mat[row][col]);
        }
    }
    return result.flat();
};
module.exports = findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);