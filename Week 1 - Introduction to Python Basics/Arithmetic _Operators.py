
print("                                                                                                                                                    ")
print("1. Arithmetic Operators")
print("   Definition: These operators perform basic mathematical operations.")
print("   Operator | Description                     | Example")
print("   ---------|----------------------------------|----------")
print("   +        | Addition                         | 5  + 3")
print("   -        | Subtraction                      | 5  - 3")
print("   *        | Multiplication                   | 5  * 3")
print("   /        | Division                         | 5  / 3")
print("   //       | Floor Division                   | 5 // 3")
print("   %        | Modulus (Remainder)              | 5  % 3")
print("   **       | Exponentiation                   | 5 ** 3")
print("                                                                                                                                                    ")





# Prompt user for the first number
num = input("Enter the first number: ")
# Prompt user for the second number
num1 = input("Enter the second number: ")

# Convert inputs to integers
num = int(num)
num1 = int(num1)

# Perform arithmetic operations
print("            Addition                         ")
sum_result = num + num1  # Conversion is very important 
print("Result:", sum_result)

print("\n           Subtraction                      ")
sub_result = num - num1
print("Result:", sub_result)

print("\n          | Multiplication                   ")
multi_result = num * num1
print("Result:", multi_result)

print("\n          | Division                         ")
div_result = num / num1
print("Result:", div_result)

print("\n          | Floor Division                    ")
floor_result = num // num1
print("Result:", floor_result)

print("\n          | Modulus (Remainder)             ")
mod_result = num % num1
print("Result:", mod_result)

print("\n          | Exponentiation                    ")
expo_result = num ** num1
print("Result:", expo_result)

# Print all results
print("\nSummary of Results:")
print("Addition:", sum_result)
print("Subtraction:", sub_result)
print("Multiplication:", multi_result)
print("Division:", div_result)
print("Floor Division:", floor_result)
print("Modulus:", mod_result)
print("Exponentiation:", expo_result)
