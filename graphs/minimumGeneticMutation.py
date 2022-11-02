# https://leetcode.com/problems/minimum-genetic-mutation/

from collections import deque

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        bank = set(bank)

        visited = set()
        q = deque([(start, 0)])

        while q:
            
            gene, level = q.popleft()
            if gene == end :
                return level

            for i in range (len(gene)):
                for choices in "ACGT":
                    new_gene = gene[:i] + choices + gene[i+1: ]
                    if new_gene in bank and new_gene not in visited:
                        q.append((new_gene, level+1))
                        visited.add(new_gene)

        return -1