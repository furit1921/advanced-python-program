def reccur_factorial(n):
    if n == 1:
        return n
    else:
        return n * reccur_factorial(n-1)

num = int(input("Enter a number to find its factorial or you will get songs about robots: "))
if num < 0:
   print("no put a positive number or i will be sad and sing you a song about robots")
elif num == 0 or num == 1:
    print("the factor of ",num,"is 1 ")
else:
    print("the factor of ",num," is ",reccur_factorial(num))