#Scope of a variable
def add():
    a=7  #Local Variable
    b=12 #Local Variable
    print(a+b)
add()

a=10    #Global variable
b=5     #Global variable 
print(a+b)


#Quiz
x=10

def change_x():
    x=20
change_x()

print(x)