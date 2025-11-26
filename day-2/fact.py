a = int(input("Enter a number: "))
b = 1
for i in range(a,0,-1):
    b = b*i
print(f"Factorial of {a} is {b}.")