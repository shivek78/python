# In Python, we have a predefined function called print for displaying output on the screen.
print("It's the output on the screen.")

# To take input from the user, we use the input() function.
number = input("Enter the number: ")  
print(number)
print(type(number))

# By default, input() takes the value as a string.
# To handle this, we can convert it to an integer using int().
# Here’s how to do that:
number = int(input("Enter the number: "))  # Convert the input to an integer
print(number) 
print(type(number)) # This will now print the number as an integer
