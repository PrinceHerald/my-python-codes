print("select operation\n1)addition\n2)subtraction\n3)multiplication\n4)division\n5)exit")
while True:
    a = int(input())
    if a<=0 or a>5:
        print("Invalid input")
    else:
        if a==5:
            print("Exited")
            break
        else:
            b = int(input())
            c = int(input())
            if a==1:
                print(b+c)
            elif a==2:
                print(b-c)
            elif a==3:
                print(b*c)
            elif a==4:
                print(b/c)