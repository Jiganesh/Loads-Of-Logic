const Test = require("../../_testconfig/Test");
const countKDifference = require("../countNumberOfPairsWithAbsoluteDifferenceK");
describe("Tests", () => {
    it("test", () => {
        Test.assertSimilar(
            countKDifference(
                [3, 2, 1, 5, 4],
                2
            ),
            3,
            "Expected value to be 3"
        );
        Test.assertSimilar(
            countKDifference(
                [1, 2, 2, 1],
                1
            ),
            4,
            "Expected value to be 4"
        );
        Test.assertSimilar(
            countKDifference(
                [1, 3],
                3
            ),
            0,
            "Expected value to be 0"
        );
    });
});
