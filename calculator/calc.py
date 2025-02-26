import math

def f(x):
    if x == 0 or x == 1 :
        return 1
    else:
        return x * f(x-1)

def f1(x,base):
    if base == 0:
        return 1
    else :
        return x * f1(x,base-1)


choice = int(input("1. Square root function - √x\n2.Factorial function - x!\n3.Natural logarithm (base е) - ln(x)\n4.Power function - x^b\nchoice : "))
while choice < 1 or choice > 4:
    choice = int(input("Wrong Choice! Choose a option between 1-4: "))
print(choice)
if choice == 1:
    num = int(input("Enter value of x : "))
    while num < 1 :
        num = int(input("cannot find square root! x should be positive : "))
    res = math.sqrt(num)
    print(f"Square root of {num} is {res}")
elif choice == 2:
    num = int(input("Enter value of x : "))
    while num < 0 :
        num = int(input("Factorial doesnot exist for values < 0! Enter non-negative values: "))
    res = f(num)
    print(f"factorial of {num} is {res}")
elif choice == 3:
    num = int(input("Enter value of x : "))
    while num <= 0 :
        num = int(input("log is undefined for x <= 0 ! Try other x : "))
    res = math.log(num)
    print(f"log (base e) of {num} is {res} ")
elif choice == 4 :
    num = int(input("Enter value of x : "))
    b = int(input("Enter value of b : "))
    while b < 0 :
        b = int(input("Base should be positive : "))
    res = f1(num,b)
    print(f"x^b for x = {num} b = {b} is {res}")

