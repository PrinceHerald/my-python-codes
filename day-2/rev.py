a = int(input("Enter a number: "))
s = ""
for i in range(len(str(a))-1,-1,-1):
    s += str(a)[i]
print(f"Reversed Number: {s}")