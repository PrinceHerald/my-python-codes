a = input("Enter a string: ")
b = 0
c = 0
for i in a:
    if ord(i)>=65 and ord(i)<=90:
        b += 1
    elif ord(i)>=97 and ord(i)<=122:
        c += 1
print(f"Uppercase letters: {b}")
print(f"Lowercase letters: {c}")