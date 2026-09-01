
n = int(input("use your laptop keys to enter a number that will be used to print a magnificent pattern that will be displayed on your screen as a star : "))

for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")

    print()