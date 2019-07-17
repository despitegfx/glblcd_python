#syntax
#lambda arguement:expression

items = [1,2,3,4,5]
print(items)

names = ["Kofi", "Kwame", "Ama"]

def sqr(x):
    return x**(2)

l=(list(map(sqr,items)))
print (l)



p = lambda x: print (x**2)
print (p(2))


fine = list(map(lambda g: g**4, items))
print (fine)


f= list (map(lambda a: "hello" + a, names))
print (f)




    




