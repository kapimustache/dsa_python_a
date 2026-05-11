def a(n):
    if n>0:
        print(f"A = {n}")
        return b(n-1)
    
def b(n):
    if n>0:
        print(f"B = {n}")
        return c(n-1)
    
def c(n):
    if n < 1:
        return n
    else: 
        print(f"C = {n}")
        return a(n-1)
    
a(5)
