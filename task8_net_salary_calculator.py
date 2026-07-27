

Task 8: Net-Salary Calculator Program
"""

HOUSE_ALLOWANCE = 6500
MEDICAL_ALLOWANCE = 5500


def calculate_paye(gross_pay):
    """c. Calculate PAYE based on gross pay bracket."""
    if gross_pay <= 15000:
        rate = 0.00
    elif gross_pay <= 30000:
        rate = 0.04
    elif gross_pay <= 50000:
        rate = 0.05
    else:
        rate = 0.06
    return gross_pay * rate


def main():
    # a. Capture employee details
    payroll_no = input("Enter payroll number: ")
    name = input("Enter employee name: ")
    gender = input("Enter gender: ")
    department = input("Enter department: ")
    basic_salary = float(input("Enter basic salary (Ksh): "))

    # b. Gross pay
    gross_pay = basic_salary + HOUSE_ALLOWANCE + MEDICAL_ALLOWANCE

    # c. PAYE
    paye = calculate_paye(gross_pay)

    # d. NHIF (2% of gross pay) and NSSF (3% of basic salary)
    nhif = gross_pay * 0.02
    nssf = basic_salary * 0.03

    # e. Total deductions and net pay
    total_deductions = paye + nhif + nssf
    net_pay = gross_pay - total_deductions

    # f. Display formatted output
    print("\n" + "=" * 40)
    print("        EMPLOYEE SALARY BREAKDOWN")
    print("=" * 40)
    print(f"Payroll No.      : {payroll_no}")
    print(f"Name             : {name}")
    print(f"Gender           : {gender}")
    print(f"Department       : {department}")
    print("-" * 40)
    print(f"Basic Salary     : Ksh {basic_salary:,.2f}")
    print(f"House Allowance  : Ksh {HOUSE_ALLOWANCE:,.2f}")
    print(f"Medical Allowance: Ksh {MEDICAL_ALLOWANCE:,.2f}")
    print(f"Gross Pay        : Ksh {gross_pay:,.2f}")
    print("-" * 40)
    print(f"PAYE             : Ksh {paye:,.2f}")
    print(f"NHIF             : Ksh {nhif:,.2f}")
    print(f"NSSF             : Ksh {nssf:,.2f}")
    print(f"Total Deductions : Ksh {total_deductions:,.2f}")
    print("-" * 40)
    print(f"NET PAY          : Ksh {net_pay:,.2f}")
    print("=" * 40)


if __name__ == "__main__":
    main()
