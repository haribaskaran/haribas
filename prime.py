l = int(input("Enter any number: "))

if l > 1:
    for i in range(2, l):
        if (l % i) == 0:
            print(l, "is not a prime number")
            break
    else:
        print("is a prime number",l)
else:
    print("is not a prime number",l)
