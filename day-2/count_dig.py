a = int(input("Enter a number: "))
b = 0
if a==0:
    print("Number of Digits is 1.")
else:
    while a!=0:
        b += 1
        a //= 10
    print(f"Number of Digits is {b}.")