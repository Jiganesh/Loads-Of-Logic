# https://www.codingninjas.com/codestudio/problems/partitions-with-given-difference_3751628?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos


def countPartitions(lenArr , difference, arr):
    # write your code here
    
    # we have to partitions such partition1 - partition2 = difference
    # we also know that partition1 + partition2 = sum(arr)
    
    # From following equations
    #  2 partition1 = difference + sum(arr)
    #  partition1 = (difference + sum(arr)) /2
    
    
    if (difference+sum(arr))% 2==1   : return 0

    sumOfPartition1 = (difference + sum(arr)) //2
    
    dp = [[0]* (sumOfPartition1+1) for i in range (len(arr)+1)]
    
    for i in range (len(arr)+1):
        for j in range(sumOfPartition1):
            if j==0:
                dp[i][j]=1
    
    for i in range (1,len(arr)+1):
        for j in range(sumOfPartition1+1):
            
            if arr[i-1]<=j:
                dp[i][j]= (dp[i-1][j]+ dp[i-1][j-arr[i-1]])%1000000007
            else :
                dp[i][j]= dp[i-1][j]%1000000007
                
    return(dp[len(arr)][sumOfPartition1])
    
print(countPartitions(4, 3,[5, 2, 6, 4]))  #1
print(countPartitions(3,1,[4,6,3])) #1
print(countPartitions(5,0,[3,1,1,2,1])) #6
print(countPartitions(4, 3,[5, 2, 6, 4])) #1
print(countPartitions(5,1,[3,2,2,5,1])) #3
print(countPartitions(4, 0, [1,1,1,1])) #6
print(countPartitions(5,7,[4,6,10,20])) #0
print(countPartitions(4, 1, [1,1,1,1])) #0



    
    
    