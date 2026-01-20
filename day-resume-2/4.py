a = int(input())
b = int(input())
c = int(input())
if ((a>b) and (a>c)):
    print(f"{a} is max")
elif ((b>a) and (b>c)):
    print(f"{b} is max")
else:
    print(f"{c} is max")