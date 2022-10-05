const Test = require("../../_testconfig/Test");
const checkIfTheSentenceIsPangram = require("../checkIfTheSentenceIsPangram");
describe("Tests", () => {
    it("test", () => {
        Test.assertEquals(
            checkIfTheSentenceIsPangram("thequickbrownfoxjumpsoverthelazydog"),
            true,
            "Expected output to be true"
        );
        Test.assertEquals(
            checkIfTheSentenceIsPangram("leetcode"),
            false,
            "Expected output to be false"
        );
    });
});