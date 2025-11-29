a1 = input("Enter dictionary 1: ")
b1 = a1.split()
d1 =  {}
for i in b1:
    key,value = i.split(":")
    d1[key] = value
a2 = input("Enter dictionary 2: ")
b2 = a2.split()
d2 =  {}
for i in b2:
    key,value = i.split(":")
    d2[key] = value
for key,value in d2.items():
    d1[key] = value
print(d1)