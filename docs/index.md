# Create a script using Exception Handling and Pickling
**Dev:** *Sherin Soman*  
**Date:** *Aug 24, 2021*  
## Introduction
Basic overview of Exception Handling and Pickling in python
## Python Exception Handling
## Python Pickling
## Code Explanation
```
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
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
        finally: # Finally block is executed
            print("Finally block for learning")
        return list_of_rows, 'Success'
```
**Code** *Function reading data from Pickle file*
## Execution
## Summary
