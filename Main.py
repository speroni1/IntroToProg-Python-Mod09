# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# James Roefs, 2020-09-09,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClassses as IO
    from DataClasses import Employee as Emp 
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
lstRows = []
lstObjects = []
fileName = "EmployeeData.txt"
strChoice = ""

# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
lstRows = P.FileProcessor.read_data_from_file(fileName)
for row in lstRows:
    lstObjects.append(Emp(row[0],row[1],row[2]))

# Show user a menu of options
while(True):
    IO.EmployeeIO.print_menu_items()
       
# Get user's menu option choice
    strChoice = IO.EmployeeIO.input_menu_options()
    
    if strChoice == '1':
    # Show user current data in the list of employee objects
        IO.EmployeeIO.print_current_list_items(lstObjects)
        continue

    elif strChoice == '2':
    # Let user add data to the list of employee objects
        emp = IO.EmployeeIO.input_employee_data()
        lstObjects.append(emp)
        continue

    elif strChoice == '3':
        P.FileProcessor.save_data_to_file(fileName,lstObjects)
        continue

    elif strChoice == '4':
        print("Goodbye!")
        print()
        break


    # let user save current data to file
    # Let user exit program

# Main Body of Script  ---------------------------------------------------- #

