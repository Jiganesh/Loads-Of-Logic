def triangle(array, result):
    result.insert(0,array)
    array = [array[i-1]+array[i] for i in range(1, len(array))]
    return triangle(array , result) if len(array)>0 else result

for i in triangle([1,2,3,4,5], []):
    print(i)
    
'''
    
    triangle(3,5,7,9)
        -> triangle (8,12,16)
            -> triangle (20 ,28)
                -> triangle (48) 
                    -> triangle () return 
                -> print(48)
            -> print(20, 28)
        ->print(8,12,16)
    ->print(3,5,7,9)
->print(1,2,3,4,5)

'''