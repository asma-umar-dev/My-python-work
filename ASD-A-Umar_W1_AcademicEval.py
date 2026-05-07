# Task: Academic Performance Evaluator
# Student: Asma Umar | Institute: As-Sa’adah Institute

print("--- Academic Performance Evaluator ---")
marks_obtained = float(input("Enter your numerical marks: "))
total_marks = 100  # Standard total

percentage = (marks_obtained / total_marks) * 100

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print("Status: Performance evaluated successfully.")
