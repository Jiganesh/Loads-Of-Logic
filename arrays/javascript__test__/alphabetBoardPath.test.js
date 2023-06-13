const Test = require("../../_testconfig/Test");
const alphabetBoardPath = require("../alphabetBoardPath");
describe("Tests", () => {
  it("test", () => {
    Test.assertEquals(
      alphabetBoardPath("leet"),
      "DDR!UURRR!!DDD!",
      "Expected to be DDR!UURRR!!DDD!"
    );
    Test.assertEquals(
      alphabetBoardPath("code"),
      "RR!DDRR!UUL!R!",
      "Expected  to be RR!DDRR!UUL!R!"
    );
    Test.assertEquals(
      alphabetBoardPath("leetcodez"),
      "DDR!UURRR!!DDD!UUULL!DDRR!UUL!R!DDDDLLLLD!",
      "Expected  to be DDR!UURRR!!DDD!UUULL!DDRR!UUL!R!DDDDLLLLD!"
    );
    Test.assertEquals(
      alphabetBoardPath("zdz"),
      "DDDDD!UUUUURRR!DDDDLLLD!",
      "Expected  to be DDDDD!UUUUURRR!DDDDLLLD!"
    );
  });
});
