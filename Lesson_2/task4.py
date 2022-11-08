number=int(input("Enter a number: "))
result=number
subtraction=number
while number>1 and subtraction>1:
    subtraction=subtraction-1
    result=result*subtraction
print("Factorial: ",result)
print("Done")