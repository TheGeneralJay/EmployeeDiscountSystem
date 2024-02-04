# TO DO:
# Fix the loop for entering an invalid input after adding new item and being prompted to create another/go back to menu.
# Placeholder data so the program does not feel empty upon first use.
employee_list = [
    [1, "Amanda Gurney", "hourly", 5, 0, 0, 1],
    [2, "Sam Relius", "manager", 5, 0, 0, 2]
]

item_list = [
    [1, "Call of Duty: Black Ops", 20],
    [2, "FFXIV: Endwalker", 60],
    [3, "Laptop", 1500]
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
                all_employee_summary()
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
    is_valid = False
    while not is_valid:
        menu_line()
        print("|                      MAKE PURCHASE                       |")
        menu_line()
        print(f"{'| Item Number':<24} {'Item Name':<23} {'Item Cost |'}")
        menu_line()

        for item in item_list:
            print(f"{'| ' + str(item[0]):<18} {item[1]:<29} {str(item[2]):<9} |")
            menu_line()

        is_valid_input = False
        while not is_valid_input:
            entered_discount_number = input("Employee Discount Number: ")

            # Ensure discount number is numeric for check.
            if int(entered_discount_number.isnumeric()):
                entered_discount_number = int(entered_discount_number)
            # If discount number exists...
            if does_employee_exist(entered_discount_number):
                # Place employee into variable.
                given_employee = get_employee(entered_discount_number)

                # Input item number.
                entered_item_number = input("Item Number: ")

                # Ensure item number is numeric for check.
                if int(entered_item_number.isnumeric()):
                    entered_item_number = int(entered_item_number)

                # If item number exists...
                if does_item_exist(entered_item_number):
                    # Place item into variable for easy access.
                    given_item = get_item(entered_item_number)

                    # Place discount in variable.
                    discount_amount = calculate_discount(given_employee)
                    discount_cost = calculate_discounted_cost(discount_amount, given_item[2])

                    # Maximum discount is $200.
                    if given_item[2] - discount_cost > 200:
                        discount_difference = 200
                    else:
                        discount_difference = given_item[2] - discount_cost

                    print("|                      Order Summary                       |")
                    menu_line()
                    print("Employee Name: " + given_employee[1])
                    print("Item Name: " + given_item[1])
                    print("Discount Amount: " + str((discount_amount * 100)) + "%")
                    print("Discounted Cost: $" + "%0.2f" % discount_cost)
                    print("Amount Saved: $" + "%0.2f" % discount_difference)

                    is_valid_input = True
                else:
                    print("Item does not exist.")
            else:
                print("Employee does not exist.")

        is_valid_input = False
        while not is_valid_input:

            menu_line()
            print("|                    Confirm Purchase                     |")
            menu_line()
            print("|                    1. Purchase Item.                    |")
            print("|                    2. Cancel                            |")
            menu_line()
            user_input = input("Confirm Purchase?: ")

            if user_input == "1":
                # Add one to total purchased.
                given_employee[4] += discount_cost
                # Add one to total discounts.
                given_employee[5] += discount_difference

                is_valid_input = True
                is_valid = True
            elif user_input == "2":
                menu_line()
                print("|                  Item purchase cancelled.                |")
                menu_line()
                is_valid_input = True

            else:
                print("Invalid input.")

        is_valid_input = False
        while not is_valid_input:
            print("|                  Purchase Different Item?                |")
            menu_line()
            print("|                 1. Purchase Different Item.              |")
            print("|                 2. Exit to Menu.                         |")
            menu_line()

            user_input = input("Purchase a Different Item?: ")
            if user_input == "1":
                menu_line()
                print("|      Press Enter to return to the item purchase menu.    |")
                menu_line()
                input()

                is_valid_input = True
            elif user_input == "2":
                menu_line()
                print("|          Press Enter to return to the main menu.         |")
                menu_line()
                input()

                is_valid_input = True
                is_valid = True
            else:
                print("Invalid input")


# --------------------------------------------------------------------------------------------------------
def all_employee_summary():
    menu_line()
    print("|                     EMPLOYEE SUMMARY                     |")
    menu_line()

    for employee in employee_list:
        print(str(employee[0]) + " | " + employee[1] + " | " + employee[2] + " | " + str(employee[3]) + " | $" + str(employee[4]) + " | $" + str(employee[5]) + " | " + str(employee[6]))
        menu_line()


# --------------------------------------------------------------------------------------------------------
def does_employee_exist(emp_disc_number):

    # Returns true if emp discount number exists within the employee_list.
    # Returns false if it does not.
    for employee in employee_list:
        if emp_disc_number == employee[6]:
            return True
    return False


# --------------------------------------------------------------------------------------------------------
def get_employee(emp_disc_number):
    for employee in employee_list:
        if emp_disc_number == employee[6]:
            return employee


# --------------------------------------------------------------------------------------------------------
def get_item(item_number):
    for item in item_list:
        if item_number == item[0]:
            return item


# --------------------------------------------------------------------------------------------------------
def does_item_exist(item_number):
    # Returns true if item number exists within the item_list.
    # Returns false if it does not.
    for item in item_list:
        if item_number == item[0]:
            return True
    return False


# --------------------------------------------------------------------------------------------------------
def calculate_discount(employee):
    if employee[3] >= 5:
        discount = 0.10
    elif employee[3] == 4:
        discount = 0.08
    elif employee[3] == 3:
        discount = 0.06
    elif employee[3] == 2:
        discount = 0.04
    elif employee[3] == 1:
        discount = 0.02
    else:
        discount = 0

    if employee[2] == "manager":
        discount += 0.10

    return discount


# --------------------------------------------------------------------------------------------------------
def calculate_discounted_cost(discount, cost):
    discounted_cost = cost - (cost * discount)
    return discounted_cost


# --------------------------------------------------------------------------------------------------------
# Program
show_menu()
