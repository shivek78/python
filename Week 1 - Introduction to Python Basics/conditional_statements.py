
#overview of conditional statements in Python, 

"""Conditional Statements in Python
Definition:
Conditional statements are constructs in programming that allow for decision-making based on specific conditions. They enable the execution of certain blocks of code when a particular condition is met (evaluates to True) and can direct the flow of execution in a program.

"""


print("""Summary:
if: Executes a block of code if the condition is true.
else: Executes a block of code if the condition in the if statement is false.
elif: Checks additional conditions if the previous if statement was false.
Nested conditionals allow for complex decision-making structures.
Logical operators help combine conditions to refine decision logic.
The ternary operator simplifies conditional assignments.
""")
"""
1. if Statement
Definition:
The if statement is used to execute a block of code only if a specified condition is true.
"""
# Define a variable 'age'
age = 18

# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are eligible to vote.")  # Execute this line if the condition is true

"""
2. if...else Statement
Definition:
The if...else statement provides an alternative block of code that runs when the if condition evaluates to false.
"""

# Define a variable 'age'
age = 16

# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are eligible to vote.")  # Execute this line if the condition is true
else:
    print("You are not eligible to vote.")  # Execute this line if the condition is false
    '''
3. if...elif...else Statement
Definition:
The if...elif...else statement allows for multiple conditions to be checked in sequence, executing the block of code for the first condition that evaluates to true.
'''

# Define a variable 'age'
age = 20

# Check multiple conditions for age
if age < 13:
    print("You are a child.")  # Execute if age is less than 13
elif age < 18:
    print("You are a teenager.")  # Execute if age is between 13 and 17
else:
    print("You are an adult.")  # Execute if age is 18 or older
    """
4. Nested Conditional Statements
Definition:
Nested conditional statements refer to placing an if statement inside another if statement, allowing for more complex decision-making.
"""

# Define variables for age and citizenship
age = 25
citizenship = "USA"

# Check if the person is eligible to vote based on age
if age >= 18:
    # Check if the person is a citizen of the USA
    if citizenship == "USA":
        print("You can vote in the USA.")  # Execute if both conditions are true
    else:
        print("You cannot vote in the USA.")  # Execute if age is 18 or older but not a citizen
else:
    print("You are not eligible to vote.")  # Execute if age is less than 18
    """
5. Logical Operators
Definition:
Logical operators (and, or, not) are used to combine multiple conditions in a single if statement, allowing for more complex conditions to be evaluated.
"""

# Define variables for age and student status
age = 20
is_student = True

# Check if the person is eligible for a student discount
if age < 18 and is_student:
    print("You get a student discount.")  # Execute if both conditions are true
else:
    print("You do not get a student discount.")  # Execute if any condition is false
'''
6. Ternary Conditional Operator
Definition:
The ternary operator provides a shorthand way to write conditional expressions, allowing for compact conditional assignments.
'''

# Define a variable 'age'
age = 15

# Use the ternary operator to determine the status
status = "Teenager" if age < 18 else "Adult"  # Assign "Teenager" if true, else "Adult"
print(status)  # Output the status
'''
Example Program
Definition:
The following example program demonstrates how to take user input and use conditional statements to determine the user's age category.

'''
# Take user input for age
age = int(input("Enter your age: "))  # Convert input to integer

# Check age category and print corresponding message
if age < 13:
    print("You are a child.")  # Execute if age is less than 13
elif age < 18:
    print("You are a teenager.")  # Execute if age is between 13 and 17
elif age < 65:
    print("You are an adult.")  # Execute if age is between 18 and 64
else:
    print("You are a senior citizen.")  # Execute if age is 65 or older

