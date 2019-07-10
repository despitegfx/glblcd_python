#Two functions to display name and age 

#get_age function takes only integers
def get_age():
    age = int(input("Enter your age: "))
    return (print("You are" ,age, "years old"))

#get_name function takes only strings
def get_name():
    name = str(input("Enter your name: "))
    return (print(name, "is yor name."))

#print both functions
print (get_name(),get_age())

