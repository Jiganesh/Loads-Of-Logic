# https://leetcode.com/problems/network-delay-time/
# Reference  :
# https://leetcode.com/problems/network-delay-time/discuss/283711/Python-Bellman-Ford-SPFA-Dijkstra-Floyd-clean-and-easy-to-understand
# https://www.youtube.com/watch?v=FtN3BYH2Zes

class Solution(object):
    
    
    # Runtime: 1161 ms, faster than 8.40% of Python online submissions for Network Delay Time.
    # Memory Usage: 15.3 MB, less than 97.48% of Python online submissions for Network Delay Time.
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        
        dist = [float("inf")]*n
        
        dist [k-1] = 0
        
        
        for _ in range (n-1):
            
            for u, v, w in times:
                
                dist[v-1] = min( dist[u-1]+w , dist[v-1])
                
        return max(dist) if max(dist)!= float("inf") else -1