from collections import defaultdict


class TrieNode :
    def __init__(self):
        self.children = defaultdict (TrieNode)
        self.isword = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isword = True
        

    def search(self, word: str) -> bool:

        node = self.root
        for ch in word:
            if ch not in node.children: return False

            node = node.children[ch]
            
        return node.isword
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for ch in prefix:
            if ch not in node.children : return False

            node = node.children[ch]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)