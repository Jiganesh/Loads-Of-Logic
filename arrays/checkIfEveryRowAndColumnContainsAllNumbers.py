#https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/


def checkValid(matrix):

# Runtime: 972 ms, faster than 59.35% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.
# Memory Usage: 14.9 MB, less than 31.63% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.

    # n =len(matrix)
    # columneach=[]
    # for i in range(n):
    #     for j in range(n):
    #         columneach.append(matrix[j][i])
        
    #     for p in range(1, n+1):
    #         if p not in columneach or p not in matrix[i]:
    #             return False
    #     columneach=[]
            
    # return True

# Runtime: 724 ms, faster than 98.14% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.
# Memory Usage: 14.8 MB, less than 32.12% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.

    # n=len(matrix)
    # check_arr=[i for i in range(1,n+1)]

    # for i in range(n):
    #     if sorted(matrix[i])!=check_arr:
    #         return False
    # for i in range(n):
    #     if sorted([row[i] for row in matrix])!=check_arr:
    #         return False


# Runtime: 716 ms, faster than 98.79% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.
# Memory Usage: 14.8 MB, less than 59.95% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.

    n=len(matrix)
    check_arr=set(i for i in range(1,n+1))
    for i in range(n):
        if set(matrix[i])!=check_arr:
            return False 
    for i in list(zip(*matrix)):
        if set(i)!=check_arr:
            return False
    return True

print(checkValid([[1,2,3],[3,1,2],[2,3,1]]))
print(checkValid([[1,1,1],[1,2,3],[1,2,3]]))