# Writh a function that can perform add, view and quit
# Author : Andre Machado

def student_display():
    print("What would you like to do? ")
    print("\t (a) Add a new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

choice = student_display()
print(f"you chose {choice}")