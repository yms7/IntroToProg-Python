# ------------------------------------------------------------------------ #
# Title: Yong Son Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What): Yong Son, 11-14-2020, Complete "To Do" list
# <Yong Son>,<11-14-2020>,Added code to "To Do" section to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts,
# load any data from text file called ToDoList.txt into the list of dictionaries rows
try:
    dicFile = open(objFile, "r")
    print("Current To-do list saved in file: ")
    for row in dicFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        print(dicRow)
        lstTable.append(dicRow)
    dicFile.close()
except:
    print("No Data saved in file")

# -- Input/Output -- # # Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if len(lstTable) == 0:
            print("There are no data saved in the table.")
        else:
            for objRow in lstTable:
                print(objRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = str(input("To Do Item: "))
        strPriority = str(input("Priority: "))
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Input data saved in the table")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strData = str(input("Enter the task you want to delete: "))
        for objRow in lstTable:
            for myKey, myValue in objRow.items():
                if (strData.lower() == myValue.lower()):
                    print("Following Row of data will be deleted: ", objRow)
                    lstTable.remove(objRow)
                else:
                    continue
            continue
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        dicFile = open(objFile, "w")
        for objRow in lstTable:
            dicFile.write(objRow["Task"] + ',' + objRow["Priority"] + '\n')
        dicFile.close()
        print("Data table has been saved to ToDoList.txt")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
