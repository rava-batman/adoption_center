def main():
    student = get_student()
    
    print(f"\n{student[0]}, has been assigned to: {student[1]} Hall! 🎉")

def get_student():
    student_name = input("Student name: ")
    assigned_dorm = input("Drom assigned: ")

    return [student_name, assigned_dorm]

main()