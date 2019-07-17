def fib_rec(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)
        

print(list(range(1,11)))
print(list(map(fib_rec, range(1,11))))