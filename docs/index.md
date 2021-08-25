# Create a script using Exception Handling and Pickling
*Sherin Soman*  
*Aug 24, 2021*  
*Assignment 07*  
## Introduction
This Assignment gives a basic overview of Exception Handling and Pickling in python. In this Assignment, I explained the steps I have done to create a script using custom functions and binary files. I start my program by loading the data in a binary file called ToDoFile.dat into a python list of dictionaries rows. The script continues to display a menu of choices to the user until the user ask to exit the program. I used a printed "menu" to guide the user through this process.

## Python Exception Handling
Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the
statements that handle the exception are written inside except clause.  

### *Catching Specific Exception*
A try clause can have any number of except clauses to handle different exceptions, however, only one will be executed in case an exception occurs. ValueError, TypeError, ZeroDivisionError, FileNotFoundError are some examples.
### *Try with Else Clause*
In python, we can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.
### *Finally Keyword in Python*
Python provides a keyword finally, which is always executed after the try and except blocks. 
### *Raising Exceptions in Python*
In Python programming, exceptions are raised when errors occur at runtime. We can also manually raise exceptions using the raise keyword.

## Python Pickling
The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) is called pickling or serialization or flattening or marshalling. We can converts the byte stream (generated through pickling) back into python objects by a process called as unpickling.  
Pickling and unplickling can be done only after importing pickle module using the command − import pickle.  
Once the file is opened for writing(wb-write binary mode), you can use pickle.dump(), which takes two arguments: the object you want to pickle and the file to which the object has to be saved. To read data from pickle file(rb-read binary mode),we can use the pickle.load()which takes one argument: the file from which binary data is read.
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
This task is defined by a function which returns the list of dictionary rows. To read data from a binary file, the file is opened in “rb” mode. Using the pickle load(), the data from the pickle file is read and loaded into the list. Two exceptions are handled while reading data from file. Specific exception,if the file to read is not found and generic exception, if the file to read is corrupted.
```     
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
 ```
**Listing 2:** *Function reading data from file and returning the list of dictionary rows*
### *Writing List data to binary file*  
This function accepts two parameters, file_name(binary file to which the list data is written) and list_of_rows(list from which data is read). The file is opened in the "wb" mode and using the pickle dump(), the data from the list is written to the binary file.

```    
    def write_data_to_file(file_name, list_of_rows):
        """ Writing data to binary file from list of dictionary rows

        :param file_name: (string) with name of binary file:
        :param list_of_rows: (list) you want to read data and write to file:
        :return: (list) of dictionary rows:
        """
        file = open(file_name, "wb")
        pickle.dump(list_of_rows,file)
        file.close()
        return list_of_rows, 'Success
 ```
**Listing 3:** *Function writing List data to a binary file*

## Execution
With the script created in its proper location, I run the script in both PyCharm (Figure 1) and an OS command/shell window (Figure 2).

![alt text](https://github.com/SherinJoel/IntroToProg-Python-Mod07/blob/main/docs/Output1.png "tooltip text")
**Figure 1.1:** *The results of Listing 2*  

![alt text](https://github.com/SherinJoel/IntroToProg-Python-Mod07/blob/main/docs/Output2.png "tooltip text")  
**Figure 1.2:** *The results of Listing 3*

![alt text](https://github.com/SherinJoel/IntroToProg-Python-Mod07/blob/main/docs/Output3.png "tooltip text")
**Figure 2:** *The Script running in Command Window*

## Verifying the result
Locate the file and open it in a text editor.  
![alt text](https://github.com/SherinJoel/IntroToProg-Python-Mod07/blob/main/docs/Output4.png "tooltip text")  
**Figure 3:** *Verifying that the file contains binary data*

## Summary
In this assignment, I was able to write a python script which uses Exceptions and Pickling. The script is executed both in PyCharm and in command window to verify the results and the script ran as expected.  I also post the files on a public GitHub repository to review.
