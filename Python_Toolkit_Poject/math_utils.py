import math

def prime_checker():
    num = int(input("Enter the number :- "))
    if num < 2:
        print("Not Prime")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not Prime Number")
                break
        else:
            print("Prime Number")

def factorial_calculator():
    num = int(input("Enter the number to find the factorial :- "))
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print(f"factorial of {num} is {fact}")

def fibonacci():
    n = int(input("Enter the number :- "))
    a, b = 0, 1
    c = 1
    seq = []
    for _ in range(n):
        seq.append(a)
        # a, b = b, a+b
        a = b
        b = c
        c = a + b
    print("Fibonacci Seq. :- ", seq)


def gcd_lcm():
    a = int(input("Enter first number :- "))
    b = int(input("Enter second number :- "))
    gcd = math.gcd(a,b)
    lcm = abs(a*b)//gcd
    print(f"GCD : {gcd} and LCM : {lcm}")