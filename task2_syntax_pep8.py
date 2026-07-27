

Task 2: Python Syntax, Zen of Python & PEP 8

This script demonstrates PEP 8 style conventions (4-space indentation,
snake_case naming, lines kept under 79 characters), single-line comments,
a module docstring, and several variable assignments.

Zen of Python (run `import this` in a Python shell to see the full poem).
Two principles explained below:

1. "Beautiful is better than ugly."
   Python encourages writing code that is clean and readable, not just
   code that works. Clear variable names and consistent formatting make
   a program easier to understand at a glance.

2. "Simple is better than complex."
   When there are multiple ways to solve a problem, Python favours the
   straightforward solution over a clever but confusing one. This keeps
   code easier to maintain and debug.
"""

# --- Variable assignments using snake_case (PEP 8 naming) ---

student_name = "Shem"          # string assignment
student_age = 22                # integer assignment
course_fee = 45000.50            # float assignment

# --- A few more assignments to show different ways of assigning values ---
first_number, second_number = 10, 20   # multiple assignment on one line
total_score = first_number + second_number
is_registered = True

# --- Demonstrating a PEP 8 friendly function ---


def describe_student(name, age, fee):
    """Return a short, formatted description of a student.

    Follows PEP 8: snake_case function/parameter names, 4-space
    indentation, and each line kept within 79 characters.
    """
    message = (
        f"{name} is {age} years old and has paid a course fee "
        f"of Ksh {fee:.2f}."
    )
    return message


if __name__ == "__main__":
    # Single-line comments like this one explain what the code below does.
    print(describe_student(student_name, student_age, course_fee))
    print(f"first_number + second_number = {total_score}")
    print(f"is_registered = {is_registered}")
