# https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    
    def maximumImportance(self, n: int, roads) -> int:
        
        dictionary= [ 0 for i in range (n)]
        for a, b in roads:
            dictionary[a]+=1
            dictionary[b]+=1
            
        def sorting_roads(x):
            return dictionary[x]
        
        roadsdic = [i for i in range (n)]
        roadsdic.sort(key = sorting_roads)
        
        lookup = {roadsdic[i]: i+1 for i in range(len(roadsdic))}
        
        
        res = 0
        for a,b in roads:
            res+= (lookup[a]+lookup[b])
        return res
        
    # Runtime: 1571 ms, faster than 100.00% of Python3 online submissions for Maximum Total Importance of Roads.
    # Memory Usage: 39.6 MB, less than 100.00% of Python3 online submissions for Maximum Total Importance of Roads.
        
    def maximumImportance(self, n: int, roads) -> int:
        
        dictionary= [ 0 for i in range (n)]
        for a, b in roads:
            dictionary[a]+=1
            dictionary[b]+=1
           
        dictionary.sort()

        result = 0
        for i in range (len(dictionary)):
            result += (i+1) * dictionary[i]
        
        return result
            
    # More Pythonic Code
    
    # Runtime: 3143 ms, faster than 33.33% of Python3 online submissions for Maximum Total Importance of Roads.
    # Memory Usage: 39.3 MB, less than 100.00% of Python3 online submissions for Maximum Total Importance of Roads.
    
    def maximumImportance(self, n: int, roads) -> int:
        
        dictionary= [ 0 for i in range (n)]
        for a, b in roads:
            dictionary[a]+=1
            dictionary[b]+=1
           
        dictionary.sort()

        return sum ([(importance+1) *count  for importance, count in enumerate(dictionary)] )
            
        
        
                   
            
            
        