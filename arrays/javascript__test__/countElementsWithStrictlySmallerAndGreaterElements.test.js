const Test = require("../../_testconfig/Test");
const countElements = require("../countElementsWithStrictlySmallerAndGreaterElements");
describe("Tests", () => {
    it("test", () => {
        Test.assertSimilar(
            countElements(
                [-3, 3, 3, 90]
            ),
            2,
            "Expected value to be 2"
        );
        Test.assertSimilar(
            countElements(
                [11, 7, 2, 15]
            ),
            2,
            "Expected value to be 3"
        );
        Test.assertSimilar(
            countElements(
                [1, 2, 3, 4, 5, 6]
            ),
            4,
            "Expected value to be 3"
        );
        Test.assertSimilar(
            countElements(
                [1, 2, 3, 4, 5, 6, 7]
            ),
            5,
            "Expected value to be 4"
        );
        Test.assertSimilar(
            countElements(
                [1, 2, 3, 4, 5, 6, 7, 8]
            ),
            6,
            "Expected value to be 4"
        );
        });
            
});
