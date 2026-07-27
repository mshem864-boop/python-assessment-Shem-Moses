

Task 5: Functions in Python
"""

# a. Built-in functions: len(), max(), sorted()
numbers = [4, 9, 1, 7, 3]
print("a. len():", len(numbers))
print("   max():", max(numbers))
print("   sorted():", sorted(numbers))


# b. User-defined function
def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width


print("\nb. Area of rectangle (5 x 3):", calculate_area(5, 3))


# c. Function with default parameter values
def greet(name, greeting="Hello"):
    """Greet a person, using a default greeting if none is given."""
    return f"{greeting}, {name}!"


print("\nc. With default:", greet("Shem"))
print("   Without default:", greet("Shem", "Welcome"))


# d. *args - sum a variable number of arguments
def sum_all(*args):
    """Return the sum of any number of arguments."""
    return sum(args)


print("\nd. sum_all(1, 2, 3):", sum_all(1, 2, 3))
print("   sum_all(4, 5, 6, 7, 8):", sum_all(4, 5, 6, 7, 8))

# e. lambda function to square a number, used with map()
square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print("\ne. Squared numbers:", squared_numbers)

# f. Variable scope: local vs global, using the global keyword
counter = 0    # global variable


def increment_counter():
    """Modify the global counter using the 'global' keyword."""
    global counter
    counter += 1
    local_message = "I only exist inside this function"  # local variable
    return local_message


print("\nf. counter before:", counter)
print("   local variable returned:", increment_counter())
print("   counter after:", counter)
