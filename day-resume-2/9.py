bal = 1000
while True:
    print("1)Withdrawl\n2)Balance check\n3)deposit\n4)exit")
    a = int(input("Select: "))
    if a<=0 or a>4:
        print("Invalid Input.")
    else:
        if a==1:
            b = int(input("Enter amount to be withdrawed: "))
            if b>bal:
                print("Insufficient Funds.")
            else:
                print(f"Amount {b} withdrawed.")
                bal -= b
        elif a==2:
            print(f"Current Balance: {bal}")
        elif a==3:
            c = int(input("Enter Amount to be Deposited: "))
            print(f"Amount {c} Deposited.")
            bal += c
        else:
            print("Exited.")
            break