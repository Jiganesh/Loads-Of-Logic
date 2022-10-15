const Test = require("../../_testconfig/Test");
const findDiagonalOrder = require("../diagonalTraverse");
describe("Tests", () => {
    it("test", () => {
        Test.assertSimilar(
            findDiagonalOrder(
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
            ),
            [1, 2, 4, 7, 5, 3, 6, 8, 9],
            "Expected value to be [1, 2, 4, 7, 5, 3, 6, 8, 9]"
        ),
            Test.assertSimilar(
                findDiagonalOrder(
                    [
                        [1, 2],
                        [3, 4]
                    ]
                ),
                [1, 2, 3, 4],
                "Expected value to be [1, 2, 3, 4]"
            ),
            Test.assertSimilar(
                findDiagonalOrder(
                    [
                        [1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20]
                    ]
                ),
                [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 17, 13, 9, 5, 10, 14, 18, 19, 15, 20],
                "Expected value to be [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 17, 13, 9, 5, 10, 14, 18, 19, 15, 20]" 
            ),
    });
});
