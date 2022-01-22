targetSum = 100
array = [25,99,59,79,20]
result=[]


def possibleSum (array, targetSum,subarray=[], memo={}):
    
    global result
    
    if targetSum-sum(subarray) in memo:
        subarray+=memo[targetSum-sum(subarray)]
    
    if subarray and sum(subarray)==targetSum:
        result.append(subarray)
    if subarray and sum(subarray)> targetSum:
        return
    for i in array: 
        memo[sum(subarray)] = subarray
        possibleSum(array, targetSum, subarray+[i], memo)
        
possibleSum(array,targetSum)
print(result)
        
    
    