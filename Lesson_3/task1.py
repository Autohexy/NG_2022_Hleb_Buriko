
def fnumber():
    number1 = float(input("Enter the first number: "))
    return number1

def snumber():
    number2 = float(input("Enter the second number: "))
    return number2


s = str(input("Enter the action: + - * / ^ r "))

def add(x,y):
    res = x+y
    print(res)

def sub(x,y):
    res = x-y
    print(res)

def mult(x,y):
    res = x*y
    print(res)

def divi(x,y):
    res = x/y
    print(res)
def r(x,y):
    res = x**y
    print(res)

def root(x):
    res=math.sqrt(x)
    print(res)

if s == "+":
    add(x, y)

elif s == "-":
    sub(x, y)

elif s == "*":
    mult(x, y)

elif s == "/":
    divi(x, y)

elif s == "^":
    r(x,y)

elif s == "r":
    root(x)








