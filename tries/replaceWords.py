# https://leetcode.com/problems/replace-words/
from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        lookup = set(dictionary)

        words = sentence.split(" ")
        for ind, word in enumerate(words):

            for j in range (1,len(word)):
                if word[:j] in lookup:
                    words[ind] = word[:j]
                    break

        return " ".join(words)