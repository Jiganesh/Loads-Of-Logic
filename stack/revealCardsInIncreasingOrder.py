# https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        N = len(deck)

        indexes = deque([i for i in range(N)])
        ordering = [0] * N

        deck.sort()

        time = 0

        while indexes:

            top_card = indexes.popleft()
            ordering[top_card] = time
            time +=1

            if indexes:
                top_card = indexes.popleft()
                indexes.append(top_card)

        return [deck[i] for i in ordering]
