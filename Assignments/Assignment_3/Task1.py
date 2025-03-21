

def fact(n):
    if n<2:
        return 1
    return n*(fact(n-1))

num = int(input("Enter the number:"))
print("Factorial of number",num,"is",fact(num))