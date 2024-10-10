print("---------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------")
print("2. Comparison Operators")
print("   Definition: These operators compare two values and return a Boolean result (True or False).")
print("   Operator | Description                     | Example")
print("   ---------|----------------------------------|----------")
print("   ==       | Equal to                         | 5 == 3")
print("   !=       | Not equal to                     | 5 != 3")
print("   >        | Greater than                     | 5 > 3")
print("   <        | Less than                        | 5 < 3")
print("   >=       | Greater than or equal to         | 5 >= 3")
print("   <=       | Less than or equal to            | 5 <= 3\n")
print("                                                                                                                                                    ")
print("---------------------------------------------------------------------------------------")
"""10 practice program 

Equal Check: Write a program that checks if two numbers provided by the user are equal.

Greater Than or Less Than: Create a program that takes two numbers and determines which one is greater or if they are equal.

Age Comparison: Ask the user for their age and compare it with a specific age (e.g., 18) to check if they are an adult or not.

Password Match: Write a program that asks the user to enter a password twice and checks if both entries match.

Temperature Comparison: Create a program that takes two temperature readings and compares them to determine which one is higher or if they are equal.

Grade Evaluation: Write a program that asks the user for their score and compares it with predefined grade thresholds (e.g., A, B, C) to determine the grade.

Discount Eligibility: Create a program that checks if a user’s total purchase amount qualifies for a discount based on a specific threshold (e.g., $100).

Voting Eligibility: Ask the user for their age and check if they are eligible to vote based on a minimum age requirement (e.g., 18).

Number Range Check: Write a program that checks if a user-provided number is within a specific range (e.g., 1 to 100).

String Comparison: Create a program that compares two strings entered by the user and checks if they are identical, or if one is lexicographically greater than the other."""
print(" (1.) Equal Check: Write a program that checks if two numbers provided by the user are equal.")
print("---------------------------------------------------------------------------------------")
#taking the value from user
num= input("enter the firsts number")
num1= input("enter the second number")
#num2=input("enter the third number")
#coverstion string to intger
num=int(num)
num1=int(num1)
print(num,num1)
if num==num1:
     
      print(" enter number is equal")
else:
      print("enter number is not equal")
print("---------------------------------------------------------------------------------------")
print(""" (2.)  Greater Than or Less Than: Create a program that takes two numbers and determines
       which one is greater or if they are equal.""")
print("---------------------------------------------------------------------------------------")
num2= input("enter the firsts number")
num4= input("enter the second number")

#coverstion string to intger
num2=int(num2)
num4=int(num4)
print("your enter no. is ",num2,num4)
if num2>num4:
      print("first number is greater ",num2)
else:
      print("second number is  greater ",num4)

print("---------------------------------------------------------------------------------------")
print("""(4.)
      Password Match: Write a program that asks the user to enter a password twice and checks if both entries match.""")
print("---------------------------------------------------------------------------------------")
pasword= input("enter  your password")
pasword1=input("enter  your password again")


#coverstion string to intger

pasword=int(pasword)
pasword1=int(pasword1)


print("youe enter password:",pasword1,pasword)
if pasword!=pasword1:
      print("password does not match",pasword,pasword1)
elif pasword==pasword:
      print("you password is match" ,pasword,pasword1)

print("---------------------------------------------------------------------------------------")
print("""(5.)
Grade Evaluation: Write a program that asks the user for their score and compares it with predefined grade thresholds (e.g., A, B, C) to determine the grade.
""")
print("---------------------------------------------------------------------------------------")

# Asking for user input for marks in three subjects
print("Enter your marks for three subjects:")
math = input("Enter your Math marks: ")
python = input("Enter your Python marks: ")
java = input("Enter your Java marks: ")

# Converting string input to integers
math = int(math)
python = int(python)
java = int(java)

print("\nYou entered marks: Math =", math, ", Python =", python, ", Java =", java)

# Grade evaluation for Math
if math >= 90:
    print("Math: You got an A grade with", math, "marks")
elif math > 70:
    print("Math: You got a B grade with", math, "marks")
elif math > 60:
    print("Math: You got a C grade with", math, "marks")
else:
    print("Math: Try next time, you got", math, "marks")

# Grade evaluation for Python
if python >= 90:
    print("Python: You got an A grade with", python, "marks")
elif python > 70:
    print("Python: You got a B grade with", python, "marks")
elif python > 60:
    print("Python: You got a C grade with", python, "marks")
else:
    print("Python: Try next time, you got", python, "marks")

# Grade evaluation for Java
if java >= 90:
    print("Java: You got an A grade with", java, "marks")
elif java > 70:
    print("Java: You got a B grade with", java, "marks")
elif java > 60:
    print("Java: You got a C grade with", java, "marks")
else:
    print("Java: Try next time, you got", java, "marks")



  