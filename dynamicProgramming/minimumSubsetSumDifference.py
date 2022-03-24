# Solution : https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10&ab_channel=AdityaVerma
# Question : https://www.codingninjas.com/codestudio/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?leftPanelTab=0 

def minimumSubsetSumDifference (arr):

    maxEleFromSubset = sum (arr)

    dp = [ [0]*(maxEleFromSubset+1) for i in range (len(arr)+1)]


    # Finding which numbers are possible from subset
    for i in range (len(arr)+1):
        for j in range (maxEleFromSubset+1):
            if i == 0 :
                dp [i][j]= False
            if j ==0:
                dp[i][j]= True

    for i in range (1, len(arr)+1):
        for j in range (maxEleFromSubset+1):
            if arr[i-1]<= j :
                dp[i][j]=  dp[i-1][j] or dp [i-1][j - arr[i-1]]
            else :
                dp[i][j]=  dp[i-1][j]


    # Uncomment to view dp matrix
    # for i in dp :
    #     for j in i:
    #         print(j ,end ="  ")
    #     print()


    # Possible Numbers from subset
    numbersPossibleFromSubset = []
    for i in range (maxEleFromSubset+1):

        if dp[len(arr)][i] :
            numbersPossibleFromSubset.append(i)

    print( numbersPossibleFromSubset)


    # Ofc the minimum difference will be present in middle
    mid = len(numbersPossibleFromSubset)//2
    s1 = numbersPossibleFromSubset[mid]
    s2 = maxEleFromSubset-s1
    

    return abs(s2-s1)

print(minimumSubsetSumDifference([1,2,7])) # 7 , 2+1
print(minimumSubsetSumDifference([2,3,7,8,10])) # 7+8 , 10+2+3
print(minimumSubsetSumDifference([7,7,7,7,7,7])) # 7+7+7 , 7+7+7
print(minimumSubsetSumDifference([1, 5, 6, 98, 84]))  #98     84+6+5+1