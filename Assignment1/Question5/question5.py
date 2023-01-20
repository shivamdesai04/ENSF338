def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n > 1:
        return lucas(n-2) + lucas(n-1)	    

print(lucas(0))
print(lucas(1))
