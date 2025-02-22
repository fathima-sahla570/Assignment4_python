#1 Write a code example using len()to find the length of  a list
num_1=[1,2,4,7,6,9,8,70,69]
print(len(num_1))
# 2. Function to greet a user
def greet():
    name=input("Enter your name")
    print("Hello", name)
greet()
# 3. Function to find the maximum value in a list without using max()
def find_maximum(numbers):
    if not numbers:  # Check if the list is empty
        return None
    max_value = numbers[0]  # Assume the first element is the largest
    for num in numbers:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found
    return max_value

# Example Usage
nums = [3, 7, 2, 9, 5]
print(find_maximum(nums))

# Explain the difference between local and global variables in a Python function.
# Write a program where a global variable and a local variable have the same name and show how Python differentiates between them.

x = 10  # Global variable

def example_function():
    x = 5  # Local variable
    print("Inside function, x =", x)  # Refers to local x

example_function()
print("Outside function, x =", x)  # Refers to global x
x = 10

def modify_global():
    global x
    x = 20  # Modifies the global variable

modify_global()
print("After function call, x =", x)
# Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
# If only the length is provided, the function should assume the width is 5.
# Show how the function behaves when called with and without the width argument.
def calculate_area(length, width=5):
    return length * width

# Example Usage
print(calculate_area(10))
print(calculate_area(10, 7))


