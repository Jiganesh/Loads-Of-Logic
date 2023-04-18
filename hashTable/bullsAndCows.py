# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret) # same length guess and secret

        # how many b 
        b = 0
        for ind in range (n):
            if secret[ind] == guess[ind]:
                b+=1

        # how many numbers same 
        a = 0
        guess_c = Counter(guess)
        secret_c = Counter(secret)

        for ind in range (n):
            key = guess[ind]
            a += min(guess_c[key], secret_c[key])
            guess_c[key]=0
            secret_c[key]=0

        c = a-b

        
        return "{}A{}B".format(b, c)

