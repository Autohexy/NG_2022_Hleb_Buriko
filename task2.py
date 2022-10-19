a=int(input("Input a number: "))
action=(input("Input an action +; -; /; *; ^; sqrt; : "))

if action=="+":
    b=int(input("Input a second number: "))
    print("Result", str(a+b))
elif action=="-":
    b=int(input("Input a second number: "))
    print("Result", str(a-b))
elif action=="/":
    b=int(input("Input a second number: "))
    print("Result", str(a/b))
elif action=="*":
    b=int(input("Input a second number: "))
    print("Result", str(a*b))
elif action=="^":
    print("Result ", str(a**2))
elif action=="sqrt":
    print("Result", str(a**0.5))

else:
    print("NaN")

    

