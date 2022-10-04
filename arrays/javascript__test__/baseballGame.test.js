const Test = {
  assertSimilar: require("assert").deepStrictEqual,
  assertEquals: require("assert").strictEqual,
};

const baseballGame = require("../baseballGame");
describe("Tests", () => {
  it("test", () => {
    Test.assertEquals(
      baseballGame(["5", "2", "C", "D", "+"]),
      30,
      "Expected array to be [1,2]"
    );
    Test.assertEquals(
      baseballGame(["5", "-2", "4", "C", "D", "9", "+", "+"]),
        27,
      "Expected array to be [1,3]"
    );
    Test.assertEquals(
      baseballGame(["3", "-4", "C", "D", "9", "+", "+"]),
      57,
      "Expected array to be [3,5]"
    );
    Test.assertEquals(
      baseballGame(["1", "C"]),
      0,
      "Expected array to be [0,1]"
    );
  });
});