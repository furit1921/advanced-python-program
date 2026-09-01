num = int(input("type number to check if it's prime"))

if num <= 1:
    print("not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("not prime")

            break
    else:
        print("prime")

        