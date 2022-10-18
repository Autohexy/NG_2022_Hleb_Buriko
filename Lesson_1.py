a=int(input("Input a number: "))
b=int(input("Input a second number: "))
action=int(input("Input an action 1=+; 2=-; 3=/; 4=*; : "))

if action==1:
    print("Result", str(a+b))
elif action==2:
    print("Result", str(a-b))
elif action==3:
    print("Result", str(a/b))
elif action==4:
    print("Result", str(a*b))
else:
    print("NaN")

    

