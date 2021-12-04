#### What is Time Complexity ?
Time Complexity is not equal to Time Taken 

Old Machine Take 10 sec to search a  non existing number in array of 10 elements , 20 sec in 20 elements , 3 sec in 30 elements

New Machine Takes 1 sec to search a non existing number in array 10 elements , 2 sec in 20 elements , 3 sec in 30 elements

Over here time is growing linearly as size is growing. This graph is Time Complexity, This Mathematical Function is Time Complexity.


<span  style ="color: blue">Time Complexity is function that gives us the relationship about  how the time will grow as the input grows.</span>

#### What do we consider when thinking about complexity ?
Always look for worst case complexities.
Always look at complexity for large data
We care about how time will vary with data
Always ignore less domination terms and constants

#### Maths
 f(N) = O ( g(N) )


#### Big O Notations (upper  bound) 
(f growth is not faster than g)

lim      _f_(N)__ < inf
N->inf    g (N)


#### Big Omega Notations (lower bound)

lim      _f_(x)__ > 0
N->inf    g (x)


#### What if an algo has lower bound  and upper bound

Theta Notation

0 < lim     _f_(x)__ < inf
    N->inf   g (x)>

#### little o Notation 
(f growth is strictly slower than g)

Big O Notation        Little o Notation (stronger statement)
f = O(g)                 f = o(g)
f <= g                    f < g

#### little omega Notation
(f is strictly greater than g)

Big Omega                    Little omega Notation
f >= g                             f > g


#### Space Complexity 
Space Complexity = Auxilary Space + Space Used By Input

We always talk about Auxilary Space
Space Complexity for Recursion = Height of Tree


2 Types of Recursion :
Linear : Fibonacci F(N) =  F(N-1)+F(N-2)
Divide and Conquer: Binary Search F(N) = F(N/2) + O(1)
(Master's Theorem taught in Uni)


#### How to solve to get complexity
- plug and chug method
- Masters Theorem
- Akra Bazzi Formula (1996)

#### Akra Bazzi Formula

<img src="Images\akraBazziFormula.png">

<img src ="Images\whatIsP.png">
<img src ="Images\PlessThanGxPart1.png">
<img src ="Images\PlessThanGxPart2.png">
<img src = "Images\linearRecurrence.png">

[Youtube Video](https://www.youtube.com/watch?v=mV3wrLBbuuE&list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&index=20)


