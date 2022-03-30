class Solution:
    
    # Runtime: 72 ms, faster than 34.08% of Python3 online submissions for Search a 2D Matrix.
    # Memory Usage: 14.6 MB, less than 8.89% of Python3 online submissions for Search a 2D Matrix.
    
    def searchMatrix(self, matrix, target):
        
        
        def binarySearch (matrix, row , cstart, cend, target):
            
            while cstart <= cend :
                cmid = cstart +(cend-cstart)//2
                if (matrix[row][cmid]==target): return True
                elif matrix[row][cmid]<target : cstart = cmid+1
                else: cend = cmid-1
            return False
        
        
        rows = len(matrix)
        cols = len(matrix[0])-1
        
        
        rstart  = 0
        rend = len(matrix)-1
        
        if (rows==1): return binarySearch(matrix, 0, 0, cols, target)
        
        cmid = cols//2
        
        while rstart < rend-1 :
            rmid = rstart+(rend-rstart)//2
            if(matrix[rmid][cmid]==target): return True
            elif matrix[rmid][cmid]< target : rstart = rmid
            else: rend = rmid
            
        if target < matrix[rstart][cmid]: return binarySearch(matrix, rstart, 0 , cmid-1, target)
        if target>=matrix[rstart][cmid] and target <= matrix[rstart][cols] : return binarySearch(matrix, rstart, cmid, cols, target)
        if target>= matrix[rend][0] and target<= matrix[rend][cmid]: return binarySearch(matrix, rend, 0, cmid, target)
        if target> matrix[rend][cmid]: return binarySearch(matrix, rend, cmid+1, cols, target)
    
        return False   
    
    
    def searchMatrix(self, matrix, target):
        
        col=len(matrix[0])    
        row=len(matrix) 
              
        start=0                 
        end=col*row-1        
        
        print("right",end)
        
        while start<=end:
            mid=(end+start)//2
            
            pointerCol=mid%col
            pointerRow=(mid-pointerCol)//col
            
            """
            Suppose of 12 elements divided in 4 columns and 3 rows
            
            If mid comes at 6
            The column where the mid will be is 6 % 4 = 2
            The row will be (6-2) //4 because it will give previous index 1 but since indexing here start from zero
            The row will be second row automatically so we can use
            
            """
            print("pointerRow",pointerRow,"pointerCol",pointerCol)
            
            if matrix[pointerRow][pointerCol]==target:
                return True
            elif matrix[pointerRow][pointerCol]<target:
                start=mid+1
            else:
                r=mid-1
        
        return False
        