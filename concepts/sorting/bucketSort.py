# RECOMMENDED : https://www.youtube.com/watch?v=ELrhrrCjDOA




import itertools
import math


def bucketSort(array):
    
    if not array : return []
    
    # edge cases when maximum is zero and numbers are negative this algorithm will not be good
    n = len(array)
    
    maximum = max(max(array, default=1),1) 
    minimum = max(min(array, default=1),1)
    
    
    ranged = math.ceil((maximum-minimum)/n)
    
    buckets = [[] for i in range (n)]
    
    # Putting Elements Into the buckets
    for num in array:
        bucket_index = math.floor((n-1) *  num / maximum)
        buckets[bucket_index].append(num)
        
    sorted_buckets = [sorted(bucket) for bucket in buckets]
    
    result = list(itertools.chain.from_iterable(sorted_buckets))
    print(result)
        
    
array1 = [3,4,4,5,2,2]
array2= [1,2,3,0,3,4,49,45,45,8,5,6,7,9,10,11,12,17,15,16]

bucketSort(array1)
bucketSort(array2)
bucketSort([])
bucketSort([0])
