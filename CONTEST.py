from collections import defaultdict
def smallString(n, s):
    
    c = defaultdict()
    left = 0
    found , result = False, s
    for right in range(n):
        while c and left< right and max(c.values()) > (right-left +1)//2:
            if right-left +1 >= 2 :
                found = True
                result = min(result, s[left:right+1], key=len)
                
            left+=1
        
        c[s[right]] = c.get(s[right], 0) + 1
    return "ZERO" if found == False else result

print(smallString(5, "abcbe"))
print(smallString(5, "aaaaa"))

        
        
        