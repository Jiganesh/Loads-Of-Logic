# https://leetcode.com/problems/longest-word-in-dictionary/
# https://www.youtube.com/watch?v=o6563NNbdtg

import collections

class TrieNode(object):
    def __init__(self):
        self.children=collections.defaultdict(TrieNode)
        self.isEnd=False
        self.word =''
        
class Trie(object):
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word):
        node=self.root
        for c in word:
            node =node.children[c]
        node.isEnd=True
        node.word=word
    
    def bfs(self):
        q=collections.deque([self.root])
        res=''
        while q:
            cur=q.popleft()
            for n in cur.children.values():
                if n.isEnd:
                    q.append(n)
                    if len(n.word)>len(res) or n.word<res:
                        res=n.word
        return res 
    
class Solution(object):
    # Runtime: 164 ms, faster than 53.74% of Python3 online submissions for Longest Word in Dictionary.
    # Memory Usage: 15.5 MB, less than 23.13% of Python3 online submissions for Longest Word in Dictionary.
    def longestWord(self, words):
        trie = Trie()
        for w in words: trie.insert(w)
        return trie.bfs()

print(Solution().longestWord(["w","wo","wor","worl","world"]))