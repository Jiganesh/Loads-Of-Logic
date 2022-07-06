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


```python

list(itertools.chain.from_iterable(sorted_buckets))
```

```python
#EdgeCase when sequence is Empty 
max([] , default = 1)

```

