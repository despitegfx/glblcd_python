#
names = ["sam", "john", "mark"]
L= (list(map(len, names)))

print (L)

print (len(names[0]))


def sqr(x):
    return x**(2)

print (sqr(4))

squares = list(map(sqr,L))
print (squares)


#bring the above into 1 line
ok=list (map(sqr,list(map(len,names))))
print (ok)





