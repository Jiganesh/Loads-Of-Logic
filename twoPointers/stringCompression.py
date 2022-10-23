# https://leetcode.com/problems/string-compression/ 

from typing import List

class Solution:
    
    # TC : O(N)
    # SC : O(N)
    def compress(self, chars: List[str]) -> int:

        current = chars[0]
        current_count = 0

        compresed_string = []

        for ch in chars:

            if ch==current:
                current_count+=1
                continue
            else:
                compresed_string.append(current)
                if current_count > 1:
                    compresed_string.append(str(current_count))

                current = ch
                current_count=1

        compresed_string.append(current)
        if current_count > 1:
            compresed_string.append(str(current_count))

        string = "".join(compresed_string)
        pointer = 0

        for ch in string:
            chars[pointer] = ch
            pointer+=1
           
        return pointer


    # TC : O(N)
    # SC : O(1)
    def compress(self, chars: List[str]) -> int:

        ch_pointer = 0
    
        n = len(chars)
        ind = 0

        while ch_pointer < n :

            current_ch = chars[ch_pointer]
            count = 0

            while ch_pointer < n and chars[ch_pointer]==current_ch:
                ch_pointer+=1
                count+=1

            chars[ind] = current_ch
            if count > 1:
                for ch in str(count):
                    ind+=1
                    chars[ind]=ch
            ind+=1

        return ind
