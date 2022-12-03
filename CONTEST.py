def somefunction(input1):
    dp = [[0 for x in range(2)] for y in range(1 << 20)]
    def countSetBits(n):
        ans = bin(n)
        return ans.count("1")

    def findMinTime(leftmask, turn, arr, n):
        if(leftmask == 0):
            return 0
        res = dp[leftmask][1 if(turn == True) else 0]
        if(~res != 0):
            return res
        rightmask = ((1 << n)-1) ^ leftmask
        if(turn == True):
            minRow = float('inf')
            person = 0
            for i in range(n):
        
                if((rightmask & (1 << i)) != 0):
                    if(minRow > arr[i]):
                        person = i
                        minRow = arr[i]
            res = arr[person] + findMinTime(leftmask | (1 << person), not turn, arr, n)
        else:
            if(countSetBits(leftmask) == 1):
                for i in range(n):
                    if((leftmask & (1 << i)) != 0):
                        res = arr[i]
                        break
            else:
                res = float('inf')
                for i in range(n):
                    if((leftmask & (1 << i)) == 0):
                        continue
                    for j in range(i+1, n):
                        if((leftmask & (1 << j)) != 0):
                            val = max(arr[i], arr[j])
                            val += findMinTime((leftmask ^ (1 << i)^ (1 << j)), not turn, arr, n)

                            res = min(res, val)
        return res
    
    def findTime(arr, n):
        mask = (1 << n) - 1
        for i in range((1 << 20)):
            dp[i][0] = -1
            dp[i][1] = -1
        return findMinTime(mask, False, arr, n)
    arr = input1
    n = len(arr)


    return findTime(arr, n)

print(somefunction([1,2,5,10]))
print(somefunction([1,2,10]))