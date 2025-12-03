a = input("Enter a string: ")
up = 0
lo = 0
for i  in a:
    if ord(i)>=65 and ord(i)<=90:
        up += 1
    elif ord(i)>=97 and ord(i)<=122:
        lo += 1
print(f"Uppercase letters: {up} , Lowercase letters: {lo}")