a = input("Enter a string: ")
if len(a)==0:
    print("String length of 0 is not allowed...")
else:
    b = ""
    count = 1
    cur = a[0]
    for i in range(1,len(a)):
        if a[i] == cur:
            count += 1
        else:
            b += (cur+str(count))
            cur = a[i]
            count = 1
    b += (cur+str(count))
    print(f"Compressed String is: {b}.")