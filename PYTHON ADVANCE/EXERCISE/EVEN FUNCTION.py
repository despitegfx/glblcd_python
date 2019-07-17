def is_even(x):
    return x%2==0

numbers = [1,56,234,87,4,76,24,69,90,135]

f = list(filter(is_even,numbers))
print (f)



#lambda f : f%2==0
g = list(filter(lambda f: f%2==0,numbers))
print (g)