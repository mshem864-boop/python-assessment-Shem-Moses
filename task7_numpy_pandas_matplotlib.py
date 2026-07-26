"""
task7_numpy_pandas_matplotlib.py

Name: Shem Moses
Registration No: T006/303998/2024
Institution: The Cooperative University of Kenya (CUK)

Task 7: Scientific Modules - NumPy, Pandas & Matplotlib

a. Install these libraries first, from the terminal (not inside this
   script):
       pip install numpy pandas matplotlib
   (also listed in requirements.txt)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# b. NumPy: 1D array of 10 numbers, mean, sum, reshape to 2x5
array_1d = np.array([12, 45, 7, 23, 56, 34, 19, 8, 41, 30])
print("b. Array:", array_1d)
print("   Mean:", array_1d.mean())
print("   Sum:", array_1d.sum())
reshaped = array_1d.reshape(2, 5)
print("   Reshaped to 2x5:\n", reshaped)

# c. NumPy: two arrays, element-wise arithmetic
array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([10, 20, 30, 40, 50])
print("\nc. array_a + array_b =", array_a + array_b)
print("   array_a - array_b =", array_a - array_b)
print("   array_a * array_b =", array_a * array_b)
print("   array_b / array_a =", array_b / array_a)

# d. Pandas: DataFrame from a dictionary, 4 columns, 5 rows of student data
student_data = {
    "name": ["Amina", "Brian", "Cynthia", "David", "Esther"],
    "admission_no": ["CU001", "CU002", "CU003", "CU004", "CU005"],
    "course": ["CS", "IT", "CS", "BIT", "CS"],
    "marks": [78, 45, 88, 63, 92],
}
df = pd.DataFrame(student_data)
print("\nd. Student DataFrame:\n", df)

# e. Pandas: filter rows where marks > 50
high_scorers = df[df["marks"] > 50]
print("\ne. Students with marks > 50:\n", high_scorers)

# f. Matplotlib: bar chart of names vs marks
plt.figure()
plt.bar(df["name"], df["marks"], color="steelblue")
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("student_marks_bar_chart.png")
print("\nf. Bar chart saved as student_marks_bar_chart.png")

# g. Matplotlib: line graph showing a trend, saved as .png
weekly_savings = [500, 700, 650, 900, 1200, 1100, 1400]
weeks = list(range(1, 8))
plt.figure()
plt.plot(weeks, weekly_savings, marker="o", color="green")
plt.title("Weekly Savings Trend")
plt.xlabel("Week")
plt.ylabel("Savings (Ksh)")
plt.tight_layout()
plt.savefig("weekly_savings_trend.png")
print("g. Line graph saved as weekly_savings_trend.png")
