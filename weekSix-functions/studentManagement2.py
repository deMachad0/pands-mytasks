#Create a program that keeps displaying the 
# menu until the user picks q. if the user chooses a then call a function called 
# doAdd() if the user chooses v then call a function called doView()
# Author: Andre Machado

def student_display():
    print("What would you like to do? ")
    print("\t (a) Add a new student")
    print("\t (v) View students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

def add():
    print("in adding")

def view():
    print("in viewing")

choice = student_display()
while(choice != 'q'):
    if choice == 'a':
        add()
    elif choice == 'v':
        view()
    elif choice != 'q':
        print("\n\n please select either a, v or q")
    choice = student_display()
