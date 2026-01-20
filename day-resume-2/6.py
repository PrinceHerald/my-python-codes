units = int(input("Enter units: "))
if units<=100:
    print("0$")
elif ((units>100) and (units<200)):
    print("5$")
else:
    print("10$")