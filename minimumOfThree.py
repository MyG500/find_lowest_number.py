# Program to find the lowest of three numbers

# Step 1: Get three numbers from the user
num1 = float(input("Enter the first number: "))  # First number
num2 = float(input("Enter the second number: "))  # Second number
num3 = float(input("Enter the third number: "))  # Third number

# Step 2: Find the lowest number among the three
lowest = min(num1, num2, num3)

# Step 3: Display the lowest number
print(f"The lowest number is: {lowest}")
