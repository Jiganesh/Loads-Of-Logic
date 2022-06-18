# https://leetcode.com/problems/prefix-and-suffix-search/

# NAIVE METHOD
class WordFilter:

    def __init__(self, words):
        self.words = words
        self.dp = {}
        

    def f(self, prefix: str, suffix: str) -> int:
        
        if (prefix, suffix) in self.dp : return self.dp[(prefix, suffix)]
        
        for i in range (len(self.words)-1,-1,-1):
            word = self.words[i]
            if word.startswith(prefix) and word.endswith(suffix):
                self.dp[(prefix, suffix)]= i
                return i
            
        self.dp [(prefix, suffix)] =-1
        return -1
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

# BEST OPTIMIZED METHOD
class WordFilter:

    def __init__(self, words):
        self.dictionary = {}
        
        for index, word in enumerate(words):
            for i in range (len(word)):
                for j in range (len(word)):
                    prefix = word[:i+1]
                    suffix = word[j:]
                    self.dictionary[prefix+"#"+suffix] = index 
        

    def f(self, prefix: str, suffix: str) -> int:
        key = prefix+"#"+suffix
        return self.dictionary[key] if key in self.dictionary else -1
        
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


# LITTLE OPTIMIZATION  : get(key, default)
class WordFilter:

    # Runtime: 1648 ms, faster than 61.47% of Python3 online submissions for Prefix and Suffix Search.
    # Memory Usage: 37.5 MB, less than 60.86% of Python3 online submissions for Prefix and Suffix Search.
    
    def __init__(self, words):
        self.dictionary = {}
        
        for index, word in enumerate(words):
            for i in range (len(word)):
                for j in range (len(word)):
                    prefix = word[:i+1]
                    suffix = word[j:]
                    self.dictionary[prefix+"#"+suffix] = index 
        

    def f(self, prefix: str, suffix: str) -> int:
        
        word = prefix+"#"+suffix
        return self.dictionary.get(word, -1)
        