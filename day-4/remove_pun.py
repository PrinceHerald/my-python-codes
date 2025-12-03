a = input("Enter a string: ")
pun = "!@#$%^&*()_-=+[]{};:'\",.<>/?|\\"
ch = ""
for i in a:
    if i not in pun:
        ch += i
print(ch)