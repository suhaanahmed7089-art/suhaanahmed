# This calculator does operations like +,-,*,/ between two numbers

print("Basic Calculator")
while True:
    num1=float(input("Enter the value of number 1: "))
    num2=float(input("Enter the value of number 2: "))

    operator=input("choose an operator(+,-,*,/): ")

    if operator in ('+','-','*',"/"):
        if operator == '+':
            print(f"Result= {num1+num2}")
        elif operator == '-':
            print(f"Result= {num1-num2}")
        elif operator == '*':
            print(f"Result= {num1*num2}")
        else:
            if num2==0:
                print("Error: cannot divide by zero")
            else:
                print(f"Result= {num1/num2}")
    else:
        print("Invalid choice, select an operator from +,-,*,/")  
