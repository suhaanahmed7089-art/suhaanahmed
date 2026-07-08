# Bill Split Calculator

print("Bill Split Calculator")

# Taking user input for bill amount and tip percentage
bill=float(input("Enter the bill amount: "))
tip_percentage=float(input("Enter the tip percentage you would like to give: "))

# Calculating tip amount and total bill(including tip)
tip_amount=(tip_percentage/100)*bill
total=bill+tip_amount
print(f"Total (including tip): ${total}")
people=int(input("Enter the no. of people sharing the bill amount: "))

# Calculating how much amount each person will pay
split_amount=total/people
print(f"Each person pays: ${split_amount}")
