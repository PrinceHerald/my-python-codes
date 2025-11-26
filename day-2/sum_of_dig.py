a = int(input("Enter a number: "))
b = 0
while a!=0:
    c = a%10
    b = b+c
    a = a//10
print(f"Sum of digits: {b}")