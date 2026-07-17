print("Welcome to Fizzbuzz!")
def fizzbuzz(num):
    num_str=str(num)
    if num%3==0 and num%7==0:
        return "Fizzbuzz"
    elif num%3==0:
        return "Fizz"
    elif num%7==0:
        return "Buzz"
    else:
        return num_str

user_input=int(input("Enter the no. of terms: "))
for i in range(1,user_input+1):
    print(fizzbuzz(i))
