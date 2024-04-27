# Student management program
# all the steps together
# Author : Andre Machado

def student_display():
    print("What would you like to do? ")
    print("\t (a) Add a new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice


def add(students):
    current_student = {}
    current_student["name"] = input("Enter name:")
    current_student["modules"] = read_modules()
    students.append(current_student)

def read_modules():
    modules = []
    module_name = input("\t Enter the first module name (blank to quit): ").strip()

    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("\t\t Enter grade:"))
        modules.append(module)
        module_name = input("\t Enter next module name (Blank to quit): ").strip()

    return modules

def display_modules(modules):
    print("\t Name  \t Grade")
    for module in modules:
        print(f"\t {module['name']}  \t {module['grade']}")

def view(students):
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])

students = []
choice = student_display()
while(choice != 'q'):
    if choice == 'a':
        add(students)
    elif choice == 'v':
        view(students)
    elif choice != 'q':
        print("\n\n please select either a, v or q")
    choice = student_display()