#https://leetcode.com/problems/pascals-triangle/

def generate(numRows):
    
    #brute force
    # rows=[[1 for i in range(n)] for n in range(1,numRows+1)]
    # for rowno in range(2,len(rows)):
    #     for ind in range(1,rowno):
    #         rows[rowno][ind]=rows[rowno-1][ind-1]+rows[rowno-1][ind]
    # return rows

    #recursive
    
    # rows=[]
    # def looped(n):
    #     if n>0:
    #         looped(n-1)
    #         rows.append([1]*n)
    #         for i in range(1, n-1):
    #             rows[n-1][i]=rows[n-2][i-1]+rows[n-2][i]            
    # looped(numRows)
    # return rows


    #with map and lambda
    # rows=[[1]]
    # for i in range(1,numRows):
    #     rows.append(list(map(lambda x,y: x+y, [0]+rows[-1], rows[-1]+[0])))
    # return rows if numRows else []
        
    # Runtime: 16 ms, faster than 99.94% of Python3 online submissions for Pascal's Triangle.
    # Memory Usage: 14 MB, less than 99.21% of Python3 online submissions for Pascal's Triangle.
    
    rows=[[1],[1,1]]
    if numRows==1:
        return [[1]]
    for r in range(2,numRows):
        prev_row=rows[r-1]
        curr_row=[1]
        for ind in range(r-1):
            curr_row+=[prev_row[ind] + prev_row[ind+1]]
        rows+=[curr_row+[1]]
    
    return rows if numRows else []
        
print(generate(5))
print(generate(0))