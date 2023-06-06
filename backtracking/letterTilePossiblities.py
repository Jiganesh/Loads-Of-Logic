# https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        lookup = Counter(tiles)
        sequence = set()
        def helper(lookup, seq,  string):


            for key , value in lookup.items():

                if value > 0:
                    lookup[key]-=1
                    seq.add(string + key)
                    helper(lookup, seq, string+key)
                    lookup[key]+=1

        helper(lookup,sequence, "" )
        result = len(sequence)

        return result
                    



