def add(a,b):
    return a + b

def sub(a,b):
    return a-b


def mult(a,b):
    return a*b

def div(a,b):
    return a/b

print("Enter the operation that you want to do:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    userchoice = input("Enter choice:" )
    first = float(input("Enter your first number: "))
    second = float(input("Enter your second number: "))

    if userchoice == '1':
        print(add(first,second))
    elif userchoice == '2':
        print(sub(first,second))
    elif userchoice == '3':
        print(mult(first,second))
    elif userchoice == '4':
        print(div(first,second))
        break 