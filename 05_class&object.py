class Student():
    def __init__(self, name, assigned_dorm):
        self.name = name
        self.assigned_dorm = assigned_dorm

def main():
    student = get_student()
    
    print(f"\n{student.name}, has been assigned to: {student.assigned_dorm} Hall! 🎉")

def get_student():    
    name = input("Student name: ")
    assigned_dorm = input("Drom assigned: ")

    return Student(name, assigned_dorm)

main()