#https://leetcode.com/problems/next-greater-element-i/

#Also known as NEAREST LARGE ELEMENT to right

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
#         brute force
#         for each element in nums2 list we scan every number on right if its greater or not

#         op=[-1]*len(nums1)
#         for i in range(len(nums2)):
#             for j in range(i,len(nums2)):
#                 if nums2[i]<nums2[j]:
#                     if nums2[i] in nums1:
#                         print(nums2[i],  nums2[j])
#                         ind=nums1.index(nums2[i])
#                         op[ind]=nums2[j]
#                         break            
#         return op


         #untill we get greater stack value, pop from stack
         #while checking if it does not get empty

         #if stack is empty, append i to stack and -1 to final
         #ie there is no greater element on right

         #if i is less than last element of stack, append it
         #it is the NEAREST LARGE ELEMENT

        
#         #Stack solution
#         from collections import deque
#         stack,final=deque() ,[-1]*len(nums1)
#         for i in nums2[::-1]:
#             if stack:
#                 while(stack and i>stack[-1]):
#                     stack.pop()
                    
#                 if not stack:
#                     stack.append(i)
                    
#                 elif i<stack[-1]:
#                     if i in nums1:
#                         #print(i, stack[-1])
#                         final[nums1.index(i)]=stack[-1]
#                     stack.append(i)
#             else:
#                 stack.append(i)
#         return final





        #Effiecient Stack solution 
        # Runtime: 40 ms, faster than 97.98% of Python3 online submissions for Next Greater Element I.
        # Memory Usage: 14.5 MB, less than 75.47% of Python3 online submissions for Next Greater Element I.
        
        from collections import deque
        stack,mapp=deque() ,{}
        
        for i in range(len(nums2)):
            
            while(stack and nums2[i]>stack[-1]):
                mapp[stack.pop()]=nums2[i]
            stack.append(nums2[i])
            
        final=[mapp.get(n,-1) for n in nums1]

        return final

        