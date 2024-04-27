# write the function doAdd(students)
# Read in the student’s name (that is straightforward)
# Read in the module names and grades  

students = []
def read_modules():
    return []

def add(students):
    current_student = {}
    current_student["name"] = input("Enter name:")
    current_student["modules"] = read_modules()

    students.append(current_student)

add(students)

add(students)
print(students)
