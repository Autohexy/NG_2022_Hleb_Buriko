first_number=int(input("Input a number: "))
action=(input("Input an action +; -; /; *; ^; sqrt; : "))

if action=="+":
    second_number=int(input("Input a second number: "))
    print("Result", str(first_number+second_number))
elif action=="-":
    second_number=int(input("Input a second number: "))
    print("Result", str(first_number-second_number))
elif action=="/":
    second_number=int(input("Input a second number: "))
    print("Result", str(first_number/second_number))
elif action=="*":
    second_number=int(input("Input a second number: "))
    print("Result", str(first_number*second_number))
elif action=="^":
    print("Result ", str(first_number**2))
elif action=="sqrt":
    print("Result", str(first_number**0.5))

else:
    print("NaN")