
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
D = b*b-4*a*c
if D < 0:
    print("D<0, Result is 0 value")
elif D == 0:
    x = -b/(2*a)
    print("Result x = ", str(x))
elif D > 0:
    x1 = (-b-D) / (2*a)
    x2 = (-b+D) / (2*a)
    print("Result: x1 = ", str(x1), "\nx2 = ", str(x2))
else:
    print("NaN")