#https://leetcode.com/problems/largest-rectangle-in-histogram/
#(Asked in Amazon SDE1 interview)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
