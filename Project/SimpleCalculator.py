def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "cannot divided by zero"
    return a / b


while True:

    print("\n------Simple Calculator------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    num1 = float(input("Enter first number :- "))
    num2 = float(input("Enter second number :- "))

    operation = input("Choose(+ , - , * , /) :- ")

    if operation == "+":
        print("Result :", add(num1,  num2))

    elif operation == "-":
        print("Result :",sub(num1, num2))

    elif operation == "*":
        print("Result :",mul(num1, num2))

    elif operation == "/":
        print("Result :",div(num1, num2))

    else:
        print("invalid operation")

    again = input("\nDo you want to continue ? (yes/no) :- ").lower()

    if again.lower() == "no":
        print("calculator closed") 
    break