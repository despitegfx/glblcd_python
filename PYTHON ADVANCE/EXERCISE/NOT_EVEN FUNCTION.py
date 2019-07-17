
numbers = [1,56,234,87,4,76,24,69,90,135]

#normal function
def is_even(x):
    return not x%2 == 0

f = list(filter(is_even,numbers))
print (f)

#lambda function
g = list(filter(lambda a: not a%2==0,numbers))
print (g)
   