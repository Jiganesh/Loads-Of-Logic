# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Solution : https://www.youtube.com/watch?v=BTf05gs_8iU

class TrieNode:
    def __init__ (self):
        self.children = {}
        self.word = False
        
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode();
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        
        currentNode = self.root
        
        for character in word:
            if character not in currentNode.children:
                currentNode.children[character]=TrieNode()
            currentNode = currentNode.children[character]
        currentNode.word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j , root):
            currentNode = root
            
            for i in range(j,len(word)):
                character = word[i]
                
                if character ==".":
                    for child in currentNode.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if character not in currentNode.children:
                        return False
                    currentNode = currentNode.children[character]
            return currentNode.word
                        
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)