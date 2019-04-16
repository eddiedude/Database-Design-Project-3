# display menu function
def display_menu():
    print("1 - Enter Display Menu")
    print("2 - Enter Search Menu")
    print("3 - Enter Modify Menu")
    print("4 - Exit")


display_menu()
flag = True
while flag:
    flag2 = input("\nEnter a command, or enter 0 to display menu: ")

    print("\n")
    if flag2 == '1':
        displayFlag = True
        print("Entering Display Menu")
        print("1 - Display all games")
        print("2 - Display all companies")
        print("3 - Display all customers")
        print("4 - Display all orders")
        while(displayFlag):
            displayinput = input("Enter a command or enter 0 to go back.\n")
            if displayinput == '1':
                print("Displaying all games")
            elif displayinput == '2':
                print("Displaying all companies")
            elif displayinput == '3':
                print("Displaying all customers")
            elif displayinput == '4':
                print("Displaying all orders")
            elif displayinput == '0':
                displayFlag = False
            else:
                print("Invalid Command")
    elif flag2 == '2':
        print("Entering Search Menu")
        print("1 - Search games by name")
        print("2 - Search games by genre")
        print("3 - Search games by company")
        searchFlag = True
        while(searchFlag):
            searchinput = input("Enter a command or enter 0 to go back.\n")
            if searchinput == '1':
                print("Search games by name")
            elif searchinput == '2':
                print("Search games by genre")
            elif searchinput == '3':
                print("Search games by company")
            elif searchinput == '0':
                searchFlag = False
            else:
                print("Invalid Command")
    elif flag2 == '3':
        print("Entering Modify Menu")
        modifyFlag = True
        print("1 - Add new game")
        print("2 - Add new company")
        print("3 - Add new customer")
        print("4 - Add new orders")
        while(modifyFlag):
            modifyinput = input("Enter a command or enter 0 to go back.\n")
            if modifyinput == '1':
                print("Adding new game")
            elif modifyinput == '2':
                print("Adding new company")
            elif modifyinput == '3':
                print("Adding new customer")
            elif modifyinput == '4':
                print("Adding new order")
            elif modifyinput == '0':
                modifyFlag = False
            else:
                print("Invalid Command")
    elif flag2 == '4':
        print("Exiting")
        flag = False
    elif flag2 == '0':
        display_menu()
    else:
        print("Invalid command.")

print("End of program")