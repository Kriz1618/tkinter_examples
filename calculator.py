# This function takes two numbers and Add togather
def add(x,y):
    return x+y
# This function takes two numbers and subtracts them.
def subtract(x,y):
    return x-y

# This function takes two numbers and multiply them.
def multiply(x,y):
    return x*y

# This function takes two numbers and divide  them.
def divide(x,y):
    return x/y
 #selection 
print("Select an Arthimatic Opration ")
print("to perform Addition select 1 ")
print("to perform Substraction select 2 ")
print("to perform Multiplication select 3 ")
print("to perform Division select 4 ")
while True:
    # accept the input from the user
    choice=input("Enter Choice (1/2/3/4): ")
    if choice in ('1','2','3','4'):
        num1=float(input('Enter first number: '))
        num2=float(input('Enter second number: '))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))

        break
    else:
        print("Invalid Input please enter again")

        

        
        

