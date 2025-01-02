units = int(input("Enter the units consumed:"))
if units>1 and units<=199:
    charge=1.20
elif units>=200 and units<400:
    charge=1.50
elif units>=400 and units<600:
    charge=1.80
else:
    charge=2.00
bill = units*charge
if bill > 400:
    bill += bill * 0.15  
if bill < 100:
    bill = 100
print("The total electricity bill is Rs:",bill)