const Test = require("../../_testconfig/Test");
const combinationSum = require("../combinationSum");
describe("Tests", () => {
    it("test", () => {
        Test.assertSimilar(
            combinationSum([2, 3, 6, 7], 7),
            [
                [2, 2, 3],
                [7],
            ],
            "Expected array to be [[7],[2,2,3]]");
            Test.assertSimilar(
                combinationSum([2, 3, 5], 8),
                [
                    [2, 2, 2, 2],
                    [2, 3, 3],
                    [3, 5],
                ],

            )
    });
});
