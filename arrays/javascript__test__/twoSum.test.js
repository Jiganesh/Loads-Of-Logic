const Test = {
  assertSimilar: require("assert").deepStrictEqual,
  assertEquals: require("assert").strictEqual,
};

const twoSum = require("../twoSum");
describe("Tests", () => {
  it("test", () => {
    Test.assertSimilar(
      twoSum([8, 3, 7, 0], 10),
      [1, 2],
      "Expected array to be [1,2]"
    );
    Test.assertSimilar(
      twoSum([1, 2, 4, 7], 9),
      [1, 3],
      "Expected array to be [1,3]"
    );
    Test.assertSimilar(
      twoSum([10, 20, 50, 100, 600, 800], 900),
      [3, 5],
      "Expected array to be [3,5]"
    );
    Test.assertSimilar(
      twoSum([1, 1, 2, 3], 2),
      [0, 1],
      "Expected array to be [0,1]"
    );
  });
});
