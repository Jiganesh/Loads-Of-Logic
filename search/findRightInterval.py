def findRightInterval(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[int]
    """
    indexedIntervals = [ intervals[i]+[i] for i in range(len(intervals)) ] #[[3, 4, 0], [2, 3, 1], [1, 2, 2]]
    indexedIntervals.sort() #[[1, 2, 2], [2, 3, 1], [3, 4, 0]]
    ans = [-1]*len(intervals)
    for i in  indexedIntervals:
        indexRightInterval = binarySearch(indexedIntervals, i[1])
        ans[i[2]] = indexedIntervals[indexRightInterval][2] if indexRightInterval != -1 else -1
        
    print(ans)
    
def binarySearch(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start+end)//2
        if array[mid][0]>=target: end = mid-1;
        else : start = mid+1;
    return start if start < len(array) else -1
             

findRightInterval([[3,4],[2,3],[1,2]])
findRightInterval([[1,2]])
findRightInterval([[1,4],[2,3],[3,4]])