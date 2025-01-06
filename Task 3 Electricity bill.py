#TASK 3
#8)Nexted if:
#Get the Electrycity UNIT from user.
#if unit is upto 199----charge is 1.20 Rs
#if unit is 200 and above but less than 400----charge is 1.50 Rs
#if unit is 600 and above ----charge is 2.00 Rs.
#find bill.
#suppose bill exceed RS. 400 the subcharge of 15% will be charged and minimum bill be should be RS. 100
#ex:
#input unit:300
#output:3450



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