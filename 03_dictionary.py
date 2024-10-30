def main():
    student = get_student()
    
    print(f"\n{student['student_name']}, has been assigned to: {student['assigned_dorm']} Hall! 🎉")

def get_student():
    a = input("Student name: ")
    b = input("Drom assigned: ")

    return {"student_name": a, "assigned_dorm": b}

main()