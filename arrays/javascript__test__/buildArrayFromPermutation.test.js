const Test = require("../../_testconfig/Test");
const buildArrayFromPermutation  = require("../buildArrayFromPermutation");
describe("Tests", () => {
    it("test", () => {
        Test.assertSimilar(
            buildArrayFromPermutation([0, 2, 1, 5, 3, 4]),
            [0, 1, 2, 4, 5, 3],
            "Expected output to be [0, 1, 2, 4, 5, 3]"
        );
        Test.assertSimilar(
            buildArrayFromPermutation([5, 0, 1, 2, 3, 4]),
            [4, 5, 0, 1, 2, 3],
            "Expected output to be [4, 5, 0, 1, 2, 3]"
        );
    });
});
