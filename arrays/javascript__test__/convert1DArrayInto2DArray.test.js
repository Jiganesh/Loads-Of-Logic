const Test = require("../../_testconfig/Test");
const construct2DArray = require("../convert1DArrayInto2DArray");
describe("Tests", () => {
    it("test", () => {
        Test.assertSimilar(
            construct2DArray(
                [1, 2, 3, 4],
                2,
                2
            ),
            [[1, 2], [3, 4]],
            "Expected value to be [1, 2, 3, 4]"

        );
        Test.assertSimilar(
            construct2DArray(
                [1, 2, 3],
                1,
                3
            ),
            [[1, 2, 3]],
            "Expected Value to be [1, 2, 3]"
        );
    });
});
