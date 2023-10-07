class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students = [
    Student("AAA", "X111", 9.3),
    Student("BBB", "X222", 7.9),
    Student("CCC", "X333", 8.2),
    Student("DDD", "X444", 7.5)
]

sorted_students = sort_students(students)

for student in sorted_students:
    print("NAME: {}, ROLL_NUMBER: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))


