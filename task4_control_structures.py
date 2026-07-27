

Task 4: Control Structures - Selection & Looping
"""


# a. if-elif-else grade classifier
def classify_grade(marks):
    """Return a letter grade for the given marks (0-100)."""
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


sample_marks = 72
print("a. Marks:", sample_marks, "-> Grade:", classify_grade(sample_marks))

# b. for loop over a list of 5 fruits
print("\nb. Fruits:")
fruits = ["mango", "banana", "apple", "orange", "grapes"]
for fruit in fruits:
    print(" -", fruit)

# c. while loop: count 1 to 10, print only even numbers
print("\nc. Even numbers from 1 to 10:")
count = 1
while count <= 10:
    if count % 2 == 0:
        print(" -", count)
    count += 1

# d. break and continue inside a loop
print("\nd. break/continue demo (numbers 1-10):")
for number in range(1, 11):
    if number == 8:
        break                      # stop the loop completely once we hit 8
    if number % 2 != 0:
        continue                   # skip odd numbers, go to next iteration
    print(" - even number before break:", number)

# e. nested loop: 3x3 multiplication table (grid layout)
print("\ne. 3x3 multiplication table:")
for row in range(1, 4):
    line = ""
    for col in range(1, 4):
        line += f"{row * col:4}"
    print(line)
