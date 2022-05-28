# https://leetcode.com/problems/sender-with-largest-word-count/
class Solution:
    
    # TC : O(N log N)
    # SC : O(N)
    
    # Runtime: 637 ms, faster than 40.00% of Python3 online submissions for Sender With Largest Word Count.
    # Memory Usage: 21.9 MB, less than 20.00% of Python3 online submissions for Sender With Largest Word Count.
    
    def largestWordCount(self, messages, senders) -> str:
        
        dictionaryOfSenders = {i :0 for i in senders}
        
        for message , sender in (zip(messages , senders)):
            dictionaryOfSenders[sender] += len(message.split(" "))
            
        return sorted([(value, key) for key , value in dictionaryOfSenders.items()])[-1][-1]
    
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 483 ms, faster than 60.00% of Python3 online submissions for Sender With Largest Word Count.
    # Memory Usage: 21.2 MB, less than 100.00% of Python3 online submissions for Sender With Largest Word Count.
    def largestWordCount(self, messages, senders) -> str:
        
        dictionaryOfSenders = {i :0 for i in senders}
        
        for message , sender in (zip(messages , senders)):
            dictionaryOfSenders[sender] += len(message.split(" "))
            
        wordCount, senderName = 0, ""
        
        for key , value in dictionaryOfSenders.items():
            if wordCount< value:
                wordCount= value
                senderName = key
            elif wordCount==value:
                senderName = max(senderName ,key)
                
                
        return senderName
            
            
        
            