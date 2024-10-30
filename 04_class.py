class Student():
    ...

def main():
    student = get_student()
    
    print(f"\n{student.name}, has been assigned to: {student.assigned_dorm} Hall! 🎉")

def get_student():
    student = Student()
    
    student.name = input("Student name: ")
    student.assigned_dormdorm = input("Drom assigned: ")

    return student

main()