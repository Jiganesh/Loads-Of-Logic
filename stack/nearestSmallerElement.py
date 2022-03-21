#https://www.interviewbit.com/problems/nearest-smaller-element/#

def NextSmallerElement(lst):
    # brute force not effcient
    # le=len(lst)
    # final=[0]*le
    # final[0]=-1
    # for i in range(le-1,-1,-1):
    #     #print("i",lst[i])
    #     for j in range(i-1,-1,-1):
    #         #print("j",lst[j])
    #         if lst[j]<lst[i]:
    #             #print(lst[j],"<",lst[i])
    #             final[i]= lst[j]
    #             #print(final)
    #             break
    #         else:
    #             final[i] = -1
    #             #print(final)

    # return final

    # Stack Solution
    sta, final = [], []
    for i in lst:
        if sta:
            #print(sta, final)
            while(sta and i <= sta[-1]):
                sta.pop()

            #print(sta, final)

            if not sta:
                final.append(-1)

            elif (i > sta[-1]):
                final.append(sta[-1])

            #print(sta, final)
        else:
            #print(sta, final)
            final.append(-1)

        sta.append(i)
    return (final)


A = [3, 2, 1]           #op= -1 -1 -1
A = [4, 5, 2, 10, 8]    #op = [-1, 4, -1, 2, 2]
print(NextSmallerElement(A))


