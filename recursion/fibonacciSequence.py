def fibonacci(terms): # terms is the amount of fibonacci terms to calculate
    if terms <= 1:
        return terms # 
    return(fibonacci(terms - 1) + fibonacci(terms - 2))

for i in range(10):
    print(fibonacci(i))
