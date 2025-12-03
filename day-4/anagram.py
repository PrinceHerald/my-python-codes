a = input("enter word 1 : ")
b = input("enter word 2 : ")
for i in range(len(a)):
    j = 0
    tr = True
    while j<len(b) and tr == True:
        if a[i]==b[j]:
            b = b[:j]+b[j+1:]
            tr = False
        j += 1
if b=="":
    print("they are anagrams")
else:
    print("They are not anagrams")