

def longestCommonSubsequence(text1, text2):
          
    dp = [[0] * (len(text1)+1) for i in range (len(text2)+1)]
    
    for pointerText2 in range (1,len(text2)+1):
        for pointerText1 in range (1,len(text1)+1):
            if text1[pointerText1-1] == text2[pointerText2-1]:
                dp[pointerText2][pointerText1] = 1 + dp[pointerText2-1][pointerText1-1]
            else:
                dp[pointerText2][pointerText1] = max(dp[pointerText2-1][pointerText1], dp[pointerText2][pointerText1-1])
    
    print(dp[-1][-1])
    return printlcs(dp, text1, text2)

    
def printlcs(dp, text1, text2):
    
    pointerText2 = len(text2)
    pointerText1 = len(text1)
    
    string = ""
    while pointerText2!=0 and  pointerText1 !=0:
        
        dp[pointerText2][pointerText1]= "*"
        
        if text1[pointerText1-1] == text2[pointerText2-1]:
            string+=text1[pointerText1-1]
            pointerText1-=1
            pointerText2-=1
            
        else:
            if dp[pointerText2-1][pointerText1] > dp[pointerText2][pointerText1-1]:
                pointerText2-=1
            else:
                pointerText1-=1
                        
        
    
                
    # Uncomment Below Line to see Path Followed   
    for i in dp : print(*i)
                
    return string[::-1]


print(longestCommonSubsequence("abac", "bvc")) 
print(longestCommonSubsequence("abcdaf", "acbcf"))
    

                
            
            
            


    
    