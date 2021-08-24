# Create a script using Exception Handling and Pickling
**Dev:** *Sherin Soman*  
**Date:** *Aug 24, 2021*  
## Introduction
Basic overview of Exception Handling and Pickling in python
## Python Exception Handling
## Python Pickling
## Create a new project in Pycharm
To create a new Project in PyCharm, I created a sub-folder called Assignment 07 inside of the _PythonClass folder and used _PythonClass\Assignment07 as its location to create the new project. Within the project, I added the python file, "Assignment07.py.
## Code Explanation
I started my script by adding the script's header.
```# ------------------------------------------------- #
# Title: Pickling and Exception Handling
# Description: A simple example of reading and writing data in a binary file
# ChangeLog: (Who, When, What)
# <SSherin>,<08.23.2021>,Created Script
# ------------------------------------------------- #
```
**Listing 1:** *Script Header*
### *Reading data from a binary file into a list of dictionary rows*
This task is defined by a function which returns the list of dictionary rows. To read data from a binary file, the file is opened in “rb” mode. Using a for loop, each row in the text file is read and splits at the specified separator (comma) using the split() method and is stored in the variables task and priority. These values are then appended to the list as dictionary rows using the append(). The file is closed using the close().
```        def read_data_from_file(file_name, list_of_rows):
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
 ```
**Listing 2:** *Function reading data from file and returning the list of dictionary rows*
## Execution

![alt text](https://github.com/SherinJoel/IntroToProg-Python-Mod07/blob/main/docs/Screen%20Shot%202021-08-24%20at%202.27.09%20PM.png "tooltip text")
#### Figure 13. The results of Listing 13
## Summary
