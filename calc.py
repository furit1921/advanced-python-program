def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("sum of 2 numbers is:", add(num1,num2))
print("difference of 2 numbers is:", minus(num1,num2))
print("times of 2 numbers is:", multiply(num1,num2))
print("quotient of 2 numbers is:", divide(num1,num2))