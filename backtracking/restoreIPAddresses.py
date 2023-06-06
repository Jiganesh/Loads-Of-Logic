# https://leetcode.com/problems/restore-ip-addresses/


from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        n = len(s)
        self.result = []

        def check (integer):
            if len(integer)>=2 and integer[0]=="0":
                return False
            return True

        def helper(last_ind, array, partition):

            integer = s[last_ind:]
            if partition==1 and integer and 0<=int(integer)<=255 and check(integer):
                array.append(s[last_ind:])
                self.result.append(".".join(array))
                array.pop()
            
            for i in range (last_ind+1, n):
                
                integer = s[last_ind:i]
                if integer and 0<=int(integer)<=255 and check(integer):
                    array.append(integer)
                    helper(i,array, partition-1)
                    array.pop()
                else:
                    break
            
        helper(0, [], 4)
        return self.result