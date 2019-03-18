def computepay(h,r):
    if(h>40):
    	pay = (h-40)*1.5*r + 40*r
    else:
    	pay = h*r
    return pay

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
print(computepay(hrs,rate))