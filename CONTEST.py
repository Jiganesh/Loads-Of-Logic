import bisect, heapq, operator, math
from typing import List
from itertools import accumulate
from collections import defaultdict, Counter, deque
from functools import lru_cache, cmp_to_key

queries = int(input())
result = 0
while queries:
    num = int(input())
    num_copy = int(num)
    initial_num_length = int(math.log10(num)+1)
    while num and num%2!=0:
        num//=10
    final_num_length = int(math.log10(num)+1) if num else initial_num_length
    
    dis = initial_num_length-final_num_length

    result += -1 if num_copy &1 and dis==0 else dis
    queries-=1
    
print(result)