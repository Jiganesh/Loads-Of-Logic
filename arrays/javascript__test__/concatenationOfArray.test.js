const Test = require("../../_testconfig/Test");
const concatenationOfArray = require("../concatenationOfArray");
describe("Tests", () => {
    it("test", () => {
        Test.assertSimilar(
            concatenationOfArray(
                [1, 2, 1]
            ),
            [1, 2, 1, 1, 2, 1]
        );
        Test.assertSimilar(
            concatenationOfArray(
                [1, 4, 7]
            ),
            [1, 4, 7, 1, 4, 7]
        );
    });
});
