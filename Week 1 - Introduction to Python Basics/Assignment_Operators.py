print("                                                                                                                                                    ")
print("4. Assignment Operators")
print("   Definition: These operators assign values to variables.")
print("   Operator | Description                     | Example")
print("   ---------|----------------------------------|----------")
print("   =        | Assigns value                   | x = 5")
print("   +=       | Adds and assigns                | x += 3 (same as x = x + 3)")
print("   -=       | Subtracts and assigns           | x -= 3")
print("   *=       | Multiplies and assigns          | x *= 3")
print("   /=       | Divides and assigns             | x /= 3")
print("   //=      | Floor divides and assigns       | x //= 3")
print("   %=       | Modulus and assigns             | x %= 3")
print("   **=      | Exponentiates and assigns       | x **= 3\n")
print("                                                                                                                                                    ")

print("""
--------------------------------------------------------------------------------------------------------------------------------------
                                                     Assignment operators
--------------------------------------------------------------------------------------------------------------------------------------
1.Counter Incrementer: Create a program that increments a counter variable each time a user enters a valid input.

2.Bank Balance Tracker: Simulate a simple bank account where users can deposit or withdraw money, updating the balance using assignment operators.

3.Score Accumulator: Build a program that tracks scores for a game, allowing users to add points for different actions and calculate the total score.

4.Age Calculator: Write a program that calculates a person's age based on the current year and their birth year, using assignment operators to update the age.

5.Temperature Log: Create a temperature logging program that allows users to input daily temperatures and calculates the total and average temperature over a week.

6.Budget Planner: Develop a budget planning app where users can set a budget and track expenses, updating the remaining budget with each expense entry.

7.Sales Tax Calculator: Write a program that calculates the sales tax on a purchase, updating the total cost with the tax using assignment operators.

8.Mileage Tracker: Build a program that tracks the distance traveled and calculates the total mileage by adding new distances entered by the user.

9.Discount Price Calculator: Create a program that applies a discount to an original price, updating the final price after applying the discount.

10.Item Quantity Tracker: Develop a program that tracks the quantity of items in stock, allowing users to add or remove items and updating the total quantity accordingly.


""")


print("""
--------------------------------------------------------------------------------------------------------------------------------------
 1.Counter Incrementer: Create a program that increments a counter variable each time a user enters a valid   input.                                                
--------------------------------------------------------------------------------------------------------------------------------------
""")
# Initialize the counter
counter = 0

# Start a loop to get user input
while True:
    user_input = input("Enter a valid input (or type '1' to quit): ")

    # Check if the user wants to exit
    if user_input == '1':
        break

    # Assuming any non-empty input is valid
    if user_input:  # This checks if the input is not empty
        counter += 1  # Increment the counter
        print(f"Valid input received! Current counter: {counter}")
    else:
        print("Invalid input. Please try again.")

print(f"Final counter value: {counter}")


print("""
--------------------------------------------------------------------------------------------------------------------------------------
2.Bank Balance Tracker: Simulate a simple bank account where users can deposit or withdraw money, updating the balance using assignment operators.
                                                 
--------------------------------------------------------------------------------------------------------------------------------------
""")