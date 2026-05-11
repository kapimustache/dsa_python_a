def direct_recursion(n):
    if n < 1: # this is the base case
        return n 
    
    print(n)
    return direct_recursion(n-1) #the recursive case

direct_recursion(5)
direct_recursion(2)