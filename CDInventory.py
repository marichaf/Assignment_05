#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Maricha Friedman, Aug 8 2021, updated to complete assignment
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        objFile = open(strFileName, 'r')
        for line in objFile:
            print(line)
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': strID, 'CD Title': strTitle, 'Artist Name': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row)
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print('Which CD would you like to delete?')
        delSrch = str(input('Enter an ID, CD Title, or Artist Name: '))
        counter = 0
        for row in lstTbl:
            for key, val in row.items(): #search in each key/value pair for delete term
                if delSrch in val:
                    lstTbl.remove(row)
                    print('\n The CD has been deleted')
                    continue
                elif delSrch not in val:
                    counter += 1
                    continue
        if counter == (len(lstTbl)*3): # multiply row length by 3 for 3 pairs of key/values in each row
            print('\nSorry,', delSrch, 'is not in the inventory')
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = str(row)
            strRow = '\n' + strRow
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

