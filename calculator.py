#FUNCTION TO CRAETE A CALCULATOR 


#CRAETING THE FUNCTIONS 
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
def avg(num1,num2):
    return num1+num2/2

# STEP 2:USER INPUT
print(
    "Please select an operation:\n"
    "1. Addition\n"
    "2. Subtraction\n"
    "3. Multiply\n"
    "4. Divide\n"
    "5. Average\n"
)
select=int(input("select the operation from 1,2,3,4,5"))
number1=int(input("Enter the first number"))
number2=int(input("Enter the second number"))

#print the result 
if select==1:
  print(number1, "+", number2, "=",\
        add(number1, number2))

elif select==2:
  print(number1, "-", number2, "=", \
        sub(number1, number2))
elif select==3:
  print(number1, "*", number2, "=", \
        multiply(number1, number2))
elif select==4:
  print(("number1, "/", number2") ,"=",\
         divide(number1, number2))
elif select==5:
  print(f"({number1} + {number2}) / 2 = {avg(number1, number2)}")
else:
  print("invalid operation you are entered please enable a correct one ")