a = input("Enter a string: ")
b = ""
for i in a:
    if i.lower()!=("a") and i.lower()!=("e") and i.lower()!=("i") and i.lower()!=("o") and i.lower()!=("u"):
        b += i
print(f"String without vowels is: {b}.")