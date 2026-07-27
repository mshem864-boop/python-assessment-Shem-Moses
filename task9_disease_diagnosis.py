

Task 9: Disease Diagnosis Program
"""

# Diagnosis lookup: symptom pairs (order-independent) mapped to a diagnosis.
DIAGNOSIS_MAP = {
    frozenset({"fever", "abdominal pain"}): "Typhoid",
    frozenset({"fever", "chills"}): "Malaria",
    frozenset({"cough", "chest pain"}): "Pneumonia",
    frozenset({"fatigue", "frequent urination"}): "Diabetes",
}


def diagnose(symptom_1, symptom_2):
    """d/e. Match a pair of symptoms to a diagnosis, or say unrecognized."""
    key = frozenset({symptom_1.lower().strip(), symptom_2.lower().strip()})
    return DIAGNOSIS_MAP.get(key, "Unrecognized symptom combination")


def main():
    # a. Welcome message
    print("Welcome to Jeshi Hospital")
    print("-" * 30)

    # b. Patient details
    name = input("Enter patient name: ")
    gender = input("Enter gender: ")
    age = input("Enter age: ")
    residence = input("Enter place of residence: ")

    # c. Capture two symptoms
    print("\nPossible symptoms include: fever, chills, abdominal pain,")
    print("cough, chest pain, fatigue, frequent urination")
    symptom_1 = input("Enter Symptom 1: ")
    symptom_2 = input("Enter Symptom 2: ")

    # d/e. Diagnose
    result = diagnose(symptom_1, symptom_2)

    # f. Formatted output
    print("\n" + "=" * 35)
    print("        DIAGNOSIS REPORT")
    print("=" * 35)
    print(f"Patient Name   : {name}")
    print(f"Gender         : {gender}")
    print(f"Age            : {age}")
    print(f"Residence      : {residence}")
    print(f"Symptom 1      : {symptom_1}")
    print(f"Symptom 2      : {symptom_2}")
    print("-" * 35)
    if result == "Unrecognized symptom combination":
        print("Result: Symptoms not recognized.")
        print("Please consult a doctor for further examination.")
    else:
        print(f"Result: Likely diagnosis - {result}")
    print("=" * 35)


if __name__ == "__main__":
    main()
