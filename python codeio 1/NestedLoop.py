#Nested Loop
n=int(input('Enter the number'))
for j in range(1,n+1):
    for i in range(1,j+1):
        print(i,end="")
    print()
