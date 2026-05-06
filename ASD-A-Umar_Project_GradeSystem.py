# Project 2: Student Grade Analyzer
# Student: Asma Umar | Institute: As-Sa’adah Institute

def get_marks():
    marks = []
    for i in range(1, 6):
        m = float(input(f"Enter marks for subject {i}: "))
        marks.append(m)
    return marks

def calculate_total(marks_list):
    return sum(marks_list)

def calculate_percentage(total):
    return (total / 500) * 100

def assign_grade(percentage, marks_list):
    # Critical Thinking Challenge: If any subject < 40, Fail
    for m in marks_list:
        if m < 40:
            return "Fail (Subject marks low)"
            
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    else: return "Fail"

def display_result():
    all_marks = get_marks()
    total = calculate_total(all_marks)
    perc = calculate_percentage(total)
    grade = assign_grade(perc, all_marks)
    
    print(f"\nTotal Marks: {total}")
    print(f"Percentage: {perc}%")
    print(f"Grade: {grade}")

# Run Project
display_result()
