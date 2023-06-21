def computepay(h,r):
    if h>40:
        h2 = h-40
        r2 = r*1.5
        pay = (40*r)+(h2*r2)
    else:
        pay = h*r
    return(print("Pay", pay))

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

computepay(h,r)