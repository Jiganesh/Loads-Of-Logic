const Test = {
    assertSimilar: require("assert").deepStrictEqual,
    assertEquals: require("assert").strictEqual,
};

const checkIfMatrixXMatrix = require("../checkIfMatrixXMatrix");
describe("Tests", () => {
    it("test", () => {
        Test.assertSimilar(
            checkIfMatrixXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]),
            true,
            "Expected output to be true"
        );
        Test.assertSimilar(
            checkIfMatrixXMatrix([[5, 7, 0], [0, 3, 1], [0, 5, 0]]),
            false,
            "Expected output to be false"
        );
    });
});
