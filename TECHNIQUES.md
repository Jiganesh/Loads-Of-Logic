- [x] cmp_to_key

```python

from functools import cmp_to_key


def cmp (x, y):
    if x < y: return -1  # negative Value if x < y them x should appear first
    if x > y  : return 1   # positive Value if x > y then x should appear last
    if x == y : return 0  # order doesn't matter
    
# Above Function Can also be written as :
def cmp(x, y):
    print(x, y , x-y)
    return x-y  # if x is smaller it will return negative value which means x should appear first
    
a = sorted([3,1,1,2], key= cmp_to_key(cmp))
print(a)
```

- [x] defaultdict

``` python
nested_dictionary = defaultdict( lambda: defaulddict(int))
```

Partitions
```python

original = [1,2,3,4]
elements = 2

array = iter(original)
matrix = [*zip(*elements*(array,))]

#matrix = [[1,2],[3,4]]

```

MOD = 10**9 +7

Extend in 2D chain

```python
list(itertools.chain.from_iterable(sorted_buckets))
```

```python
#EdgeCase when sequence is Empty 
max([] , default = 1)

```


Condition and IF TRUE or IF FALSE
```python
n = 5
result = n%2==0 and "EVEN" or "ODD"
```

fractions module 

Link : https://www.tutorialspoint.com/fraction-module-in-python
```python

from fractions import Fraction

n2 = 36
d2 = 64

num = 33.33

print(Fraction(n2, d2))  # output :  9/16
print(Fraction(num)) # output : 2345390243441541/70368744177664
print(Fraction(str(num))) # output : 3333/100
print(Fraction(0.25)) # output 1/4
print(Fraction(0.25).numerator) # output 1
print(Fraction(0.25).denominator) # output 45



```


GCD Learn From : https://www.youtube.com/watch?v=utZcJ0leZ_g

```python


a = 96
b = 64

# a is dividend
# b is divisor

def gcd (a,  b):
    
    if b ==0 : return a
    else: return gcd(b , a%b)
    
print(gcd(a, b))
```

Fractions Like GCD
```python

a = 96
b = 64


def gcd (a, b):
    if b==0 : return a 
    else : return gcd(b , a%b)
    
gcd_ab = gcd(a, b)
num = a//gcd_ab
den = b//gcd_ab

result = (num, den) # output (3, 2) and gcd_ab is 32

```


Technique for remembering a change : You can convert it to negative of its value

Copying 2D array
```python
matrix = [row[:] for row in grid]
```

Segmentation Tree :https://www.youtube.com/watch?v=I7RFycpqbDk


Number of Node in tree of  height h 
```python
number_of_nodes = 2 * (2**h)- 1
```

Transpose of a matrix 

```python
transpose_matrix = list(map(list, zip(*matrix)))
```

Find Valid Rectangles from given points
```python
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]

hashset = set(map(tuple, points))

for point1 in hashset:
    for point2 in hashset:
        
        '''point1 and point2 are diagonal with direction  \ '''

        x1, y1 = point1
        x2, y2 = point2
        
        if x1 < x2 and y1 < y2 and (x1, y2) in hashset and (x2, y1) in hashset:
            print(  "Rectangle : ", point1, (x1, y2) , (x2, y1), point2 )

```

How Counter can be used to add to add value of particular key

```python


items1 = [[1,1],[4,5],[3,8]]
items2 =  [[3,1],[1,5]]
a = Counter(dict(items1))+Counter(dict(items2))

sorted(a.items())# [(1, 6), (3, 9), (4, 5)]
```

```python

list(map(operator.add, [1,2], [1,2,3,4])) # [2, 4]
list(map(operator.sub, [1,2], [0,1,2])) # [1, 1]
```


Find the position of only set bit : formula 

```python
bit = 16
power = int(math.log10(bit) / math.log10(2))

print(power) # 4

```


Formula to Check if there is only one bit present in number

```python

number = 16
if number & (number-1) == 0:
    print("Only one bit is present")
else:
    print("More than one bit is present")

# 0b1010101010101010101010101010101 = 1431655765 = 0X55555555
```

Good Example to understand bit adding and removal
- https://leetcode.com/problems/longest-nice-subarray/

```text
Sliding window, AND is the AND result in the window.
Let's slide a subarray window and keep it nice.

If it's nice to add a new element a to the window,
AND & a should be 0,
and then we update AND |= A[j]

Otherwice we move the head out of the window by doing AND ^= A[i]
```

Fibonacci number Formula

```text

Yes, there is an exact formula for the n-th term! It is:
an = [Phin – (phi)n] / Sqrt[5].
where Phi = (1 + Sqrt[5]) / 2 is the so-called golden mean, and
phi = (1 – Sqrt[5]) / 2 is an associated golden number, also equal to (-1 / Phi). This formula is attributed to Binet in 1843, though known by Euler before him.

```

```python
d = Counter('qwertyuiop' + 'asdfghjkl' * 2 + 'zxcvbnm' * 3)
assigning index based on row of keyboard
```


```Check If all characters of string a present in string b

# Pythonic Code


# Part A        # Part B  

set("abc") <= set("abdcef") # All the elements of A are in B --> returns True
set("abcdef") <= set("abdf") # All the elements of A are in B --> returns False

```


Algorithms you should know

Boyer-Moore Voting Algorithm - problems - (Majority Element II)

![twin_prime](/.dev/maths/closestPrimeNumbersInRange.png)

Level Order Traversal Technique

```python


if not root:
    return []

q = deque([root])

while q:
    print([i.val for i in q])
    q = [child for p in q for child in [p.left, p.right] if child]

```