while True:
    print("1)Adition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit")
    a = int(input("Select: "))
    if a<=0 or a>5:
        print("Invalid Input.")
    elif a==5:
        print("Exited.")
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
