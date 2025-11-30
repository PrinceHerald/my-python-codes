a = input("Enter password: ")
if len(a)<8 or " " in a:
    print("Invalid Password...")
else:
    up = 0
    lo = 0
    di = 0
    sp = 0
    for i in a:
        if ord(i)>=65 and ord(i)<=90:
            up += 1
        elif ord(i)>=97 and ord(i)<=122:
            lo += 1
        elif ord(i)>=48 and ord(i)<=57:
            di += 1
        else:
            sp += 1
    if up>0 and lo>0 and di>0 and sp>0:
        print("Access Granted...")
    else:
        print("Invalid Password...")