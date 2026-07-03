# Student Grade Calculator

# Features:
# - Add Student
# - Display Student Records
# - Search Student
# - Update Student Marks
# - Delete Student
# - Automatic Grade Calculation

# Author: Aditya Siwach

students = []

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

def add_student():
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = []

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        while True:
            mark = float(input(f"Enter marks of subject {i+1}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

    total = sum(marks)
    average = round(total / n, 2)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")
    
def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for s in students:
            print("\nStudent Details")
            print("Name:", s["name"])
            print("Roll Number:", s["roll"])
            print("Marks:", s["marks"])
            print("Total Marks:", s["total"])
            print("Average:", s["average"])
            print("Grade:", s["grade"])

def search_student():
    roll = int(input("Enter roll number to search: "))

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found")
            print("Name:", s["name"])
            print("Roll Number:", s["roll"])
            print("Marks:", s["marks"])
            print("Total Marks:", s["total"])
            print("Average:", s["average"])
            print("Grade:", s["grade"])
            return

    print("Student not found.")

def update_student():
    roll = int(input("Enter roll number to update: "))

    for s in students:
        if s["roll"] == roll:
            new_marks = []
            n = int(input("Enter number of subjects: "))

            for i in range(n):
                mark = float(input(f"Enter new marks of subject {i+1}: "))
                new_marks.append(mark)

            s["marks"] = new_marks
            s["total"] = sum(new_marks)
            s["average"] = s["total"] / n
            s["grade"] = calculate_grade(s["average"])

            print("Student record updated successfully!")
            return

    print("Student not found.")

def delete_student():
    roll = int(input("Enter roll number to delete: "))

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")

while True:
    print("\n===== Student Grade Calculator Menu =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")




