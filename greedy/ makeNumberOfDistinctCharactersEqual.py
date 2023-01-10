# https://leetcode.com/problems/make-number-of-distinct-characters-equal/

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        def check(array1, array2):
            c1 = 0
            c2 = 0
            for i in range(26):
                c1+= bool(array1[i])
                c2+= bool(array2[i])
            return c1==c2

        def counter(word):
            array = [0]*26
            for al in word:
                ch_ind = ord(al)- ord("a")
                array[ch_ind] +=1
            return array

        w1 = counter(word1)
        w2 = counter(word2)

        for i in range(0, 26):
            for j in range(0, 26):
                
                if w1[i] and w2[j]:

                    # swap 
                    # deleting letter from w1 and putting in w2
                    w1[i]-=1
                    w2[i]+=1

                    # deleting letter from w2 and putting in w1
                    w1[j]+=1
                    w2[j]-=1

                    if check (w1, w2): return True

                    # adding letter from w2 back to w1
                    w1[i]+=1
                    w2[i]-=1

                    # adding letter from w1 back to w2
                    w1[j]-=1
                    w2[j]+=1
                            
        return False
