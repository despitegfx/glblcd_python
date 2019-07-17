#syntax
#filter(function name, list name)

def too_old(x):
    return x > 30

age = [22,25,29,34,56,24,12]

print (too_old(12))
print (too_old(40))


filter(too_old,age)

m = list(filter(too_old,age))
print (m)


def too_young(x):
    return x < 25

f= list(filter(too_young,age))
print (f)

print (too_young(22))
print (too_young(25))
