# Placeholder data so the program does not feel empty upon first use.
employee_list = [
    [1, "Amanda Gurney", "hourly", 1, 0, 0, 1]
]

item_list = [
    [1, "Call of Duty: Black Ops", 20],
    [2, "FFXIV: Endwalker", 60]
]


# --------------------------------------------------------------------------------------------------------
# Functions
# Design
def menu_line():
    print("------------------------------------------------------------")


# Menu
def show_menu():
    menu_continue = False
    while not menu_continue:
        menu_line()
        print("|               WELCOME TO YOUR GBC EMPLOYEE               |")
        print("|                       DISCOUNT TOOL                      |")
        menu_line()
        print("|                   (1) Create Employee                    |")
        print("|                   (2) Create Item                        |")
        print("|                   (3) Make Purchase                      |")
        print("|                   (4) All Employee Summary               |")
        print("|                   (5) Exit                               |")
        menu_line()
        user_option = int(input("Enter a menu option: "))
        menu_line()

        # User choice logic.
        match user_option:
            case 1:  # Create Employee
                create_employee()
            case 2:  # Create Item
                create_item()
            case 3:  # Make Purchase
                make_purchase()
            case 4:  # All Employee Summary
                all_employee_summary(employee_list)
            case 5:  # Exit
                print("|   Thank you for using Your GBC Employee Discount Tool!   |")
                print("|                  Have a fantastic day!                   |")
                menu_line()
                menu_continue = True
            case _:
                print("Invalid input.")


# Option functions.
def create_employee():
    print("temp")


def create_item():
    print("temp")


def make_purchase():
    print("temp")


def all_employee_summary(emp_list):
    print("temp")


# Program
show_menu()
