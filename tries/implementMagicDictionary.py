# https://leetcode.com/problems/implement-magic-dictionary/

from collections import defaultdict
from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isword = True

class MagicDictionary:

    def __init__(self):

        self.head = Trie()

    def buildDict(self, dictionary: List[str]) -> None:

        for word in dictionary:
            self.head.insert(word)
        

    def search(self, searchWord: str) -> bool:
        
        is_replaced = False
        node = self.head.root

        n = len(searchWord)
        def helper(node, ind, word, is_replaced):
            answer = False
            if ind == n and node.isword and is_replaced:
                return True

            if ind >= n: 
                return False


            ch = word[ind]
            for new_ch in node.children:

                
                if new_ch == ch:
                    answer |= helper(node.children[ch], ind+1, word, is_replaced)
                if new_ch != ch and is_replaced == False:
                    answer |= helper(node.children[new_ch], ind+1, word, True)
                
            return answer

        return helper(node, 0, searchWord, is_replaced)
                    
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)