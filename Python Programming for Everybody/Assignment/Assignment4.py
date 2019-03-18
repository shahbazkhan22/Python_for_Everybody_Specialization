hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hrs>=40:
    pay = (hrs-40)*1.5*rate + 40*rate
else:
    pay = hrs*rate
print(pay)