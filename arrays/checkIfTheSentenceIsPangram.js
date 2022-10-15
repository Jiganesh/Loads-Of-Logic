// https://leetcode.com/problems/check-if-the-sentence-is-pangram
// Runtime: 116 ms, faster than 21.44% of JavaScript online submissions for Check if the Sentence Is Pangram.
// Memory Usage: 42.6 MB, less than 66.74% of JavaScript online submissions for Check if the Sentence Is Pangram.
/**
 * @param {string} sentence
 * @return {boolean}
 */
const checkIfPangram = (sentence) => {
  let letters = "abcdefghijklmnopqrstuvwxyz";
  sentence
    .trim()
    .split("")
    .forEach((val) => {
      letters = letters.replace(val, "");
    });
  return letters.length === 0;
};

module.exports = checkIfPangram;
