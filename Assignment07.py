# ------------------------------------------------- #
# Title: Pickling and Exception Handling
# Description: A simple example of reading and writing data in a binary file
# ChangeLog: (Who, When, What)
# <SSherin>,<08.23.2021>,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.dat"  # The name of the binary file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a binary file into a list of dictionary rows

        :param file_name: (string) with name of binary file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        try:
            file = open(file_name, "rb")
            list_of_rows= pickle.load(file)
        except FileNotFoundError as e:
            return list_of_rows, 'File not found. Make sure to create file by saving data using option 3'
        except Exception as e:
            file.close()
            print(e, e.__doc__, type(e), sep='\n')
            return list_of_rows, 'There was an issue reading the data from file. Please try again'
        finally: # Finally block is always executed
            print("Finally block for my learning")
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Getting data from user and adding it into a list of dictionary rows

        :param task: (string) you want to add to list:
        :param priority: (string) you want to add to list:
        :return: (list) of dictionary rows:
        """
        row = {"Task": task.strip(), "Priority": priority.strip()}
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Remove a given task from list

        :param task: (string) you want to remove from list:
        :param list_of_rows: (list) from which you want to remove data:
        :return: (list) of dictionary rows:
        """
        flag=0
        for row in list_of_rows:
            if (row["Task"] == task):
                flag=1
                list_of_rows.remove(row)
                break
        if flag==0:
            return list_of_rows, 'Task could not be found'
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writing data to binary file from list of dictionary rows

        :param file_name: (string) with name of binary file:
        :param list_of_rows: (list) you want to read data and write to file:
        :return: (list) of dictionary rows:
        """
        file = open(file_name, "wb")
        pickle.dump(list_of_rows,file)
        file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets a new task and priority from the user

        :return: (string) task and priority
        """
        task = str(input("Enter the task to be done: "))
        priority = str(input("Enter the priority of the task: "))
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Gets a task to remove from the user

        :return: (string) task
        """
        task = str(input("Enter the task to be removed: "))
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()
        lstTable, strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = IO.input_task_to_remove()
        lstTable, strStatus = Processor.remove_data_from_list(strTask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
