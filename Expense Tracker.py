# Create a console based expense traker in python that allows the user to record daily expenses and
# view summary like total spending. 

# PROJECT DETAILS:
# You are required to build a simple personal finance management tool.
# the program should allow the user to :
# 1. Add an expense in details like date, category, amount and description.
# 2. View all expenses recorded.
# 3. Calculate total spending so far.
# 4. Exit the program gracefully when the user chooses to do so.
# All tasks must be implemented using loops, if-else, and dictionary only.
# No user defined functions and file handling should be used.

expenses=[]
print("Welcome to Expense Tracker Management Tool")
print("Enter your choice")
print("1. Add an expense")
print("2.View all expenses")
print("3 Calculate total spendings")
print("4. Exit")

choice=0
while True:

    # Taking user input for choice
    choice=int(input("Enter your choice: "))
    
    # Code block for adding an expense
    if(choice==1):
        # Taking user input for expense details
        date=input("Enter the date(DD-MM-YYYY):")
        category=input("Enter the type of expense(food,makeup,travel etc.):")
        amount=int(input("Enter the total spendings:"))

        expense = {
            "date":date,
            "category":category,
            "amount":amount
        }
        expenses.append(expense)
    
    # Code block for viewing all expenses
    elif(choice==2):
        if (len(expenses)==0):
            print("No expenses are stored yet")
        else:
            print("===Your Expenses===")
            count=1
            for exp in expenses:
                print(f"{count}. Date {exp["date"]}")
                print(f"{count}. Category {exp["category"]}")
                print(f"{count}. Amount {exp["amount"]}")
                count+=1
    
    # Code block for calculating total spendings
    elif(choice==3):
        total=0
        for exp in expenses:
            total=total+exp["amount"]
            print(f"Total spendings = {total}")
    
    # Code block for exiting the program
    elif(choice==4):
        print("Exit successfully")
        break

    else:
        print("Invalid choice, please try again")

