#https://leetcode.com/problems/largest-rectangle-in-histogram/
#(Asked in Amazon SDE1 interview)
# Solution : https://www.youtube.com/watch?v=vcv3REtIvEo (Noob Solution)
# Solution : https://www.youtube.com/watch?v=zx5Sw9130L0 (Pro Solution)


class Solution:
    def largestRectangleArea(self, heights):
        sta,finalL=[],[]
        it=0
        for i in heights:               #code for next smallest left
            it+=1
            if sta:
                while(sta and i<=sta[-1][1]):
                    sta.pop()

                if not sta:
                    finalL.append(-1)

                elif (i>sta[-1][1]):
                    finalL.append(sta[-1][0]-1)

            else:
                finalL.append(-1)

            sta.append([it,i])

        print("finalL",finalL)

        # general len(heights) as for reverse
        it,sta,finalR=len(heights),[],[]   #code of Next smallest right
        for i in heights[::-1]:     #it-=1 for counting index
            it-=1               #as it process in reverse    
            if sta:
                while(sta and i<=sta[-1][1]):
                    sta.pop()

                if not sta:
                    #if array empty 1 index ahead of last index
                    finalR.append(len(heights))

                elif (i>sta[-1][1]):
                    finalR.append(sta[-1][0])

            else:
                finalR.append(len(heights))

            sta.append([it,i])

        finalR=finalR[::-1]   
        print("finalR",finalR)

        final=[]        #calculate width=NSR-NSL-1 and area=width*height[k] ie arr[k]

        for k in range(len(heights)):
            final.append( (finalR[k] - finalL[k] -1) *heights[k])

        print("area",final)
        return (max(final))
    
    
    # Submitted By Jiganesh
    
    # TC : O(N)
    # SC : O(N)
    
    
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n= len(heights)
        leftSmaller , rightSmaller = [],[]* n
        
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            leftSmaller.append((stack[-1]+1) if stack else 0);
            stack.append(i)
            
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            rightSmaller[i]=(stack[-1]-1) if stack else n-1;
            stack.append(i)            
            
        maximum = 0;
        for i in range(n):
            currentArea = (rightSmaller[i] - leftSmaller[i]+1)*heights[i]
            maximum = max(maximum , currentArea)
            
        return maximum
    
    # Submitted by Jiganesh
    
    # TC : O(N)
    # SC : O(N)
    
    def largestRectangleArea(self, heights):
        maxArea =0;
        stack = []
        
        for i , h in enumerate (heights):
            start = i
            while stack and stack[-1][1]> h:
                index, height = stack.pop()
                maxArea - max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
            
        for i , h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
    
    
print(Solution().largestRectangleArea([2,1,5,6,2,3]))

