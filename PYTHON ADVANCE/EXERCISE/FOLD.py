#print length of each words in the sentence
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print ("Lenght of each word in the sentence: ",[len(word) for word in words])


#print positive numbers from the list
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
p = list (filter (lambda x: not x<-1, numbers))
print("Postive Numbers: ",p)

#function to print positive numbers from the list
for n in numbers:
    if n>0:
        print ("n: ",n)
        
 #print even numbers from the list       
numberss = [12, 54, 33, 67, 24, 89, 11, 24, 47]
for q in numberss:
    if q%2==0:
        print ("q: ",q)

 #print even numbers from the list with lamdba function
h = list(filter(lambda l: l%2==0, numberss))
print (h)


 #print even numbers from the list with other function
c = [n for n in numberss if n%2==0]
print (c)

 #print numbers which are not even from the list
numbers = range(1,50)
f = [n for n in numbers if n%2!=0]
print ("odd numbers: ",f)

 #print numbers which are not even from the list with other function
x=[n for n in numbers if n%2!=0]
print ("odd numbers: ",x)



#factorial in iteration function
def factorial(n):
    #base case 1! = 1
    
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print (factorial(5))


#print each word in the list in capital letters with its length
words = ["hello", "my", "name", "is", "Emmanuel"]
a = [len(words) for word in words]
b = [word.upper() for word in words]
print (tuple(zip(b,a)))

    