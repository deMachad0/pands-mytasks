# adding the read modules until the user enters a module name of blank
# Author: Andre Machado


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

read_modules()

