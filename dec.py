import random
def fibonacci_Generator():
    a=0
    b=1
    for i in range(n):
        yield b
        a,b= b,a+b
n=int(input("enter number to generate"))
obj = fibonacci_Generator()
for _ in range(n):
    print(next(obj),end=" ")


