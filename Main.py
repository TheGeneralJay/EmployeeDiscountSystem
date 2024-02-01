# TO DO:
# Fix the loop for entering an invalid input after adding new item and being prompted to create another/go back to menu.
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


# --------------------------------------------------------------------------------------------------------
# Basically runs the entire program.
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


# --------------------------------------------------------------------------------------------------------
# Option functions.
# create_employee() runs through adding a new employee to the employee_list.
def create_employee():
    # Loop for adding new employee if user wants to repeat the process.
    is_valid = False
    while not is_valid:
        print("|                      CREATE EMPLOYEE                     |")
        menu_line()
        print("|  Please enter the employee's information when prompted.  |")
        menu_line()
        # Employee ID validation.
        employee_id = create_validation("Employee ID: ", "id")
        if employee_id == "no":  # Exit if the user entered 'no'.
            return False

        employee_name = create_validation("Employee Name: ", "name")
        if employee_name == "no":  # Exit if the user entered 'no'.
            return False

        employee_type = create_validation("Employee Type (hourly or manager): ", "type").lower()
        if employee_type == "no":  # Exit if the user entered 'no'.
            return False

        employee_years_worked = create_validation("Employee Years Worked: ", "year")
        if employee_years_worked == "no":  # Exit if the user entered 'no'.
            return False

        employee_discount_number = create_validation("Employee Discount Number: ", "discount")
        if employee_discount_number == "no":  # Exit if the user entered 'no'.
            return False

        is_valid_input = False
        while not is_valid_input:
            print("Employee ID: " + employee_id)
            print("Employee Name: " + employee_name)
            print("Employee Type: " + employee_type)
            print("Total Years Worked: " + employee_years_worked)
            print("Employee Discount Number: " + employee_discount_number)
            menu_line()
            print("|                      Confirmation                        |")
            menu_line()
            print("|                  (1) Create Employee.                    |")
            print("|                  (2) Cancel.                             |")
            menu_line()
            user_input = input("Is this information correct?: ")

            if user_input == "1":
                employee = employee_list.append(
                    [int(employee_id), employee_name, employee_type, int(employee_years_worked), 0, 0,
                     int(employee_discount_number)]
                )
                menu_line()
                print("|               Employee added to the system.              |")
                menu_line()
                print("|                  (1) Create New Employee.                |")
                print("|                  (2) Return to Menu.                     |")
                menu_line()
                user_input = input("What would you like to do?: ")

                if user_input == "1":
                    menu_line()
                    print("|            Press Enter to create a new employee.         |")
                    menu_line()
                    input()
                elif user_input == "2":
                    menu_line()
                    print("|          Press Enter to return to the main menu.         |")
                    menu_line()

                    input()
                    return employee
                else:
                    print("Invalid input.")

                is_valid_input = True

            elif user_input == "2":
                menu_line()
                print("|                Employee creation cancelled.              |")
                print("|          Press Enter to return to the main menu.         |")
                menu_line()
                input()

                is_valid_input = True
                is_valid = True
            else:
                print("Invalid input.")


# --------------------------------------------------------------------------------------------------------
def validate_input(user_input, validation_type):
    # Checks if input is blank.
    if user_input == "" or user_input is None:
        print("Please enter a valid input.")
        return False

    # Error messages dependent on validation_type for ease-of-access.
    match validation_type:
        # Validates any numerical inputs.
        case "id" | "discount" | "year" | "item_num" | "cost":
            # If user input is not a number...
            if not user_input.isnumeric():
                # Customized errors for each type.
                match validation_type:
                    case "id":
                        print("Please enter a valid ID.")
                        return False
                    case "cost":
                        print("Please enter a valid cost.")
                        return False
                    case "discount":
                        print("Please enter a valid discount number.")
                        return False
                    case _:
                        print("Please enter a valid number.")
            else:  # If user input is a number...
                match validation_type:
                    case "id":
                        employee_id = int(user_input)
                        # Checks if employee ID already exists within employee_list.
                        for employee in employee_list:
                            if employee_id == employee[0]:
                                print("Employee with ID " + str(employee_id) + " already exists.")
                                return False
                    case "discount":
                        employee_discount_number = int(user_input)
                        # Checks if employee discount number already exists within employee_list.
                        for employee in employee_list:
                            if employee_discount_number == employee[6]:
                                print("Employee with discount number " + str(employee_discount_number) + " already exists.")
                                return False
                    case "item_num":
                        item_number = int(user_input)
                        # Checks if item number already exists within item_list.
                        for item in item_list:
                            if item_number == item[0]:
                                print("Item with item number " + str(item_number) + " already exists.")
                                return False
            return True  # Returns true if the number input passes these checks.
        case "name":
            # If name is a number...
            if user_input.isnumeric():
                print("Please enter a valid name.")
                return False
            else:
                # If any character in the name is a number...
                if any(map(str.isdigit, user_input)):
                    print("Employee name must contain only letters, spaces, and necessary symbols.")
                    return False
                # If the first character is not a letter...
                elif not user_input[0].isalpha():
                    print("Employee name must start with a letter.")
                    return False
                return True  # Returns true if the name input passes these checks.
        case "type":
            if user_input.lower() == "hourly" or user_input.lower() == "manager":
                return True
            else:
                print("Please enter either 'hourly' or 'manager'.")
                return False

    return True  # Returns True for item name.


# --------------------------------------------------------------------------------------------------------
def create_validation(input_message, validation_type):
    is_valid_input = False
    while not is_valid_input:
        user_input = input(input_message)
        menu_line()

        if user_input.lower() == "no":
            print("Exiting to main menu.")
            user_input = "no"
            return user_input

        if validate_input(user_input, validation_type):
            is_valid_input = True

    return user_input


# --------------------------------------------------------------------------------------------------------
def create_item():
    # Loop for adding new employee if user wants to repeat the process.
    is_valid = False
    while not is_valid:
        print("|                       CREATE ITEM                        |")
        menu_line()
        print("|    Please enter the item's information when prompted.    |")
        menu_line()

        # Item Number
        item_number = create_validation("Item Number: ", "item_num")
        if item_number == "no":  # Exit if the user entered 'no'.
            return False

        item_name = create_validation("Item Name: ", "item_name")
        if item_name == "no":  # Exit if the user entered 'no'.
            return False

        item_cost = create_validation("Item Cost: ", "cost")
        if item_cost == "no":  # Exit if the user entered 'no'.
            return False

        is_valid_input = False
        while not is_valid_input:
            print("Item Number: " + item_number)
            print("Item Name: " + item_name)
            print("Item Cost: " + item_cost)
            menu_line()
            print("|                      Confirmation                        |")
            menu_line()
            print("|                   (1) Create Item.                       |")
            print("|                   (2) Cancel.                            |")
            menu_line()
            user_input = input("Is this information correct?: ")

            if user_input == "1":
                item = item_list.append(
                    [int(item_number), item_name, int(item_cost)]
                )
                menu_line()
                print("|                 Item added to the system.                |")
                menu_line()
                print("|                  (1) Create New Item.                    |")
                print("|                  (2) Return to Menu.                     |")
                menu_line()
                user_input = input("What would you like to do?: ")

                if user_input == "1":
                    menu_line()
                    print("|              Press Enter to create a new item.           |")
                    menu_line()
                    input()
                elif user_input == "2":
                    menu_line()
                    print("|          Press Enter to return to the main menu.         |")
                    menu_line()

                    input()
                    return item
                else:
                    print("Invalid input.")

            elif user_input == "2":
                menu_line()
                print("|                  Item creation cancelled.                |")
                print("|          Press Enter to return to the main menu.         |")
                menu_line()
                input()

                is_valid_input = True
                is_valid = True
            else:
                print("Invalid input.")


# --------------------------------------------------------------------------------------------------------
def make_purchase():
    menu_line()
    print("|                      MAKE PURCHASE                       |")
    menu_line()
    print(f"{'| Item Number':<24} {'Item Name':<23} {'Item Cost |'}")
    menu_line()

    for item in item_list:
        print(f"{'| ' + str(item[0]):<18} {item[1]:<29} {str(item[2]):<9} |")
        menu_line()


# --------------------------------------------------------------------------------------------------------
def all_employee_summary(emp_list):
    print(employee_list)


# --------------------------------------------------------------------------------------------------------
# Program
show_menu()
