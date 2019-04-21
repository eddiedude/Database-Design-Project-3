import psycopg2
import psycopg2.extensions
import getpass as pw
import datetime

# print function

def print_companies(rs):
    print("{0:<20} {1:<20} {2:<15} {3:<20} {4:<0}".format("Name", "Founder", "Year Founded", "CEO", "Headquarters"))
    print("---------------------------------------------------------------------------------------------")
    for row in rs:
        print("{0:<20} {1:<20} {2:<15} {3:<20} {4:<0}".format(row[0], row[1], row[2], row[3], row[4]))
    
def print_games(rs):
    print("{0:<15} {1:<30} {2:<15} {3:<15} {4:<15} {5:<10} {6:<20} {7:<0}".format("GID", "Title", "Publisher", "Developer", "Genre", "Year", "System", "Price"))
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    for row in rs:
        print("{0:<15} {1:<30} {2:<15} {3:<15} {4:<15} {5:<10} {6:<20} {7:0.2f}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

def print_customers(rs):
    print("{0:<20} {1:<30} {2:<15} {3:<10} {4:<10} {5:<15} {6:<0}".format("Name", "Address", "City", "State", "Zip", "Phone Number", "CID"))
    print("----------------------------------------------------------------------------------------------------------------------")
    for row in rs:
        print("{0:<20} {1:<30} {2:<15} {3:<10} {4:<10} {5:<15} {6:<0}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

def print_orders(rs):
    print("{0:<20} {1:<20} {2:<20} {3:<15} {4:<0}".format("OID", "GID", "CID", "Sale", "Date"))
    print("---------------------------------------------------------------------------------------------")
    for row in rs:
        print("{0:<20} {1:<20} {2:<20} {3:<15.2f} {4:<0}".format(row[0], row[1], row[2], row[3], row[4].strftime('%m/%d/%Y')))
    
# selecting all values from tables

def get_games(conn):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Games";')
        rs = cur.fetchall()
        print_games(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def get_companies(conn):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Company";')
        rs = cur.fetchall()
        print_companies(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def get_customers(conn):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Customer";')
        rs = cur.fetchall()
        print_customers(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def get_orders(conn):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Orders";')
        rs = cur.fetchall()
        print_orders(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def get_sorted_orders_by_customer_id(conn):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Orders" ORDER BY "CID" ASC')
        rs = cur.fetchall()
        print_orders(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def get_sorted_orders_by_game_id(conn):
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Orders" ORDER BY "GID" ASC')
        rs = cur.fetchall()
        print_orders(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

# search by parameter functions

def search_games_by_name(conn):
    try:
        search = input("Enter a name to search by: ")
        search = search.lower().strip()
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Games" WHERE LOWER("Title") LIKE \'%' + search + '%\';')
        rs = cur.fetchall()
        print_games(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def search_games_by_genre(conn):
    try:
        search = input("Enter a genre to search by: ")
        search = search.lower().strip()
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Games" WHERE LOWER("Genre") LIKE \'%' + search + '%\';')
        rs = cur.fetchall()
        print_games(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def search_games_by_company(conn):
    try:
        search = input("Enter a company (publisher) to search by: ")
        search = search.lower().strip()
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Games" WHERE LOWER("Publisher") LIKE \'%' + search + '%\';')
        rs = cur.fetchall()
        print_games(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def search_orders_by_customer_id(conn):
    try:
        search = input("Enter a customer ID to search by: ")
        search = search.lower().strip()
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Orders" WHERE LOWER("CID") LIKE \'%' + search + '%\';')
        rs = cur.fetchall()
        print_orders(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def search_orders_by_game_id(conn):
    try:
        search = input("Enter a game ID to search by: ")
        search = search.lower().strip()
        cur = conn.cursor()
        cur.execute('SELECT * FROM public."Orders" WHERE LOWER("GID") LIKE \'%' + search + '%\';')
        rs = cur.fetchall()
        print_orders(rs)
        cur.close()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

# adding values to Games or Orders

def add_new_game(conn):
    try: 
        # verify that user has INSERT permission
        cur = conn.cursor()
        cur.execute('INSERT INTO public."Games" ("GID") VALUES (\' \');')
        cur.execute('DELETE FROM public."Games" WHERE "GID" = \' \';')
        cur.close()

        print("Enter the following information for the new game.")
        gid = input("GID: ")
        title = input("Title: ")
        publisher = input("Publisher: ")
        developer = input("Developer: ")
        genre = input("Genre: ")
        year = input("Year: ")
        system = input("System: ")
        price = input("Price: ")

        gid = gid.strip()
        title = title.replace('\'', '\'\'') # if the title contains a single quote/apostophe
        year = int(year)
        price = float(price)

        cur = conn.cursor()
        cur.execute('INSERT INTO public."Games" VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', %d, \'%s\', %f);' % (gid, title, publisher, developer, genre, year, system, price))
        conn.commit()
        print("Game added!")
        cur.close()
    except Exception as e:
        print("Something went wrong. Please make sure all entries are formatted correctly. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def add_new_company(conn):
    try: 
        # verify that user has INSERT permission
        cur = conn.cursor()
        cur.execute('INSERT INTO public."Company" ("Name") VALUES (\' \');')
        cur.execute('DELETE FROM public."Company" WHERE "Name" = \' \';')
        cur.close()

        print("Enter the following information for the new company.")
        name = input("Name: ")
        founder = input("Founder: ")
        year = input("Year Founded: ")
        ceo = input("CEO: ")
        hq = input("Headquarters: ")

        name = name.strip()
        name = name.replace('\'', '\'\'') # if the name contains a single quote/apostophe
        founder = founder.replace('\'', '\'\'')
        ceo = ceo.replace('\'', '\'\'')
        hq = hq.replace('\'', '\'\'')
        year = int(year)

        cur = conn.cursor()
        cur.execute('INSERT INTO public."Company" VALUES (\'%s\', \'%s\', %d, \'%s\', \'%s\');' % (name, founder, year, ceo, hq))
        conn.commit()
        print("Company added!")
        cur.close()
    except Exception as e:
        print("Something went wrong. Please make sure all entries are formatted correctly. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def add_new_customer(conn):
    try: 
        # verify that user has INSERT permission
        cur = conn.cursor()
        cur.execute('INSERT INTO public."Customer" ("CID") VALUES (\' \')')
        cur.execute('DELETE FROM public."Customer" WHERE "CID" = \' \';')
        cur.close()

        print("Enter the following information for the new customer.")
        name = input("Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State (abbreviation): ")
        zip = input("Zip code: ")
        phone = input("Phone number: ")
        cid = input("CID: ")

        cid = cid.strip()
        name = name.replace('\'', '\'\'') # if the string contains a single quote/apostophe
        address = address.replace('\'', '\'\'')
        city = city.replace('\'', '\'\'')

        cur = conn.cursor()
        cur.execute('INSERT INTO public."Customer" VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (name, address, city, state, zip, phone, cid))
        conn.commit()
        print("Customer added!")
        cur.close()
    except Exception as e:
        print("Something went wrong. Please make sure all entries are formatted correctly. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def add_new_order(conn):
    try: 
        # verify that user has INSERT permission
        cur = conn.cursor()
        cur.execute('INSERT INTO public."Orders" ("OID", "GID", "CID") VALUES (\' \', \' \', \' \')')
        cur.execute('DELETE FROM public."Orders" WHERE "OID" = \' \';')
        cur.close()

        print("Enter the following information for the new order.")
        oid = input("OID: ")
        gid = input("GID: ")
        customer = input("CID: ")

        oid = oid.strip()
        cur = conn.cursor()
        # verifies game is in Games table and gets price
        cur.execute('SELECT "Price" FROM public."Games" WHERE "GID" = \'' + gid + '\';')
        record = cur.fetchone()
        sale = record[0]

        # verifies cid is in Customer table
        cur.execute('SELECT "CID" FROM public."Customer" WHERE "CID" = \'' + customer + '\';')
        record = cur.fetchone()
        cid = record[0]

        cur.execute('INSERT INTO public."Orders" VALUES (\'%s\', \'%s\', \'%s\', \'%f\', CURRENT_DATE);' % (oid, gid, cid, sale))
        conn.commit()
        print("Order added!")
        cur.close()
    except Exception as e:
        print("Something went wrong. Please make sure all entries are formatted correctly. GID and CID must already exist in the system (in Games or Customers, respectively) in order to be added to Orders. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

# deleting from tables
def delete_game(conn):
    try: 
        # verify that user has permission
        cur = conn.cursor()
        cur.execute('INSERT INTO public."Games" ("GID") VALUES (\' \')')
        cur.execute('DELETE FROM public."Games" WHERE "GID" = \' \';')
        cur.close()

        gid = input("Enter the GID of the game you wish to delete EXACTLY (case sensitive): ")

        gid = gid.strip()

        cur = conn.cursor()
        cur.execute('DELETE FROM public."Games" WHERE "GID" = \'%s\';' % (gid))
        conn.commit()
        print("Game deleted!")
        cur.close()
    except Exception as e:
        print("Something went wrong. Please make sure all entries are formatted correctly. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def delete_company(conn):
    try: 
        # verify that user has permission
        cur = conn.cursor()
        cur.execute('INSERT INTO public."Company" ("Name") VALUES (\' \')')
        cur.execute('DELETE FROM public."Company" WHERE "Name" = \' \';')
        cur.close()

        name = input("Enter the name of the company you wish to delete EXACTLY (case sensitive): ")

        name = name.strip()

        cur = conn.cursor()
        cur.execute('DELETE FROM public."Company" WHERE "Name" = \'%s\';' % (name))
        conn.commit()
        print("Company deleted!")
        cur.close()
    except Exception as e:
        print("Something went wrong. Please make sure all entries are formatted correctly. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

def delete_customer(conn):
    try: 
        # verify that user has permission
        cur = conn.cursor()
        cur.execute('INSERT INTO public."Customer" ("CID") VALUES (\' \')')
        cur.execute('DELETE FROM public."Customer" WHERE "CID" = \' \';')
        cur.close()

        cid = input("Enter the CID of the customer you wish to delete EXACTLY (case sensitive): ")

        cid = cid.strip()

        cur = conn.cursor()
        cur.execute('DELETE FROM public."Customer" WHERE "CID" = \'%s\';' % (cid))
        conn.commit()
        print("Customer deleted!")
        cur.close()
    except Exception as e:
        print("Something went wrong. Please make sure all entries are formatted correctly. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

# update game (price only)
def update_game(conn):
    try: 
        # verify that user has permission
        cur = conn.cursor()
        cur.execute('INSERT INTO public."Games" ("GID") VALUES (\' \')')
        cur.execute('DELETE FROM public."Games" WHERE "GID" = \' \';')
        cur.close()

        gid = input("Enter the GID of the game whose price you are changing EXACTLY (case sensitive): ")
        price = input("Enter the updated price: ")
    
        gid = gid.strip()
        price = float(price)

        cur = conn.cursor()
        cur.execute('UPDATE public."Games" SET "Price" = %f WHERE "GID" = \'%s\';' % (price, gid))
        conn.commit()
        print("Game updated!")
        cur.close()
    except Exception as e:
        print("Something went wrong. Please make sure all entries are formatted correctly. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

# create new user
def create_new_user(conn):
    try: 
        username = input("Enter new username: ")
        password = pw.getpass("Enter new password: ")
        confirmpass = pw.getpass("Confirm new password: ")
        key = pw.getpass("Enter employee key (ignore if customer): ")
        if password != confirmpass:
            print("Passwords do not match. Please try again.")
        elif password == confirmpass and key != '1234':
            print("Creating customer account.")
            cur = conn.cursor()
            cur.execute("CREATE USER %s WITH PASSWORD '%s';" %(username, password))
            # grant permissions to customer account
            cur.execute("GRANT SELECT ON TABLE public.\"Games\" TO %s; GRANT SELECT ON TABLE public.\"Company\" TO %s;" %(username, username))
            conn.commit()
        elif password == confirmpass and key == '1234':
            print("Creating employee account.")
            cur = conn.cursor()
            cur.execute("CREATE USER %s WITH PASSWORD '%s';" %(username, password)) 
            # grant permissions to employee account
            cur.execute("ALTER USER %s CREATEROLE; GRANT INSERT, SELECT, UPDATE, DELETE ON TABLE public.\"Company\" TO %s WITH GRANT OPTION; GRANT INSERT, SELECT, UPDATE, DELETE ON TABLE public.\"Customer\" TO %s WITH GRANT OPTION; GRANT INSERT, SELECT, UPDATE, DELETE ON TABLE public.\"Games\" TO %s WITH GRANT OPTION; GRANT INSERT, SELECT, UPDATE, DELETE ON TABLE public.\"Orders\" TO %s WITH GRANT OPTION;" %(username, username, username, username, username))
            conn.commit()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

# delete existing user
def delete_user(conn):
    try: 
        print("Note: this action cannot be undone!")
        username = input("Enter the username of the user you wish to delete EXACTLY (case sensitive): ")

        cur = conn.cursor()
        # delete permissions to account and drop
        cur.execute("REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM %s; REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM %s; REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM %s; DROP USER %s;" %(username, username, username, username))
        print("User deleted!")
        conn.commit()
    except Exception as e:
        print("Something went wrong. Error: " + str(e))
        cur = conn.cursor()
        cur.execute('ROLLBACK;')
        cur.close()

'''
to drop a user after granting them privileges:
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM customer;
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM customer;
REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM customer;
DROP USER customer;
'''

# connection - asks for login info
def connection():
    try:
        username = input("Enter Username: ")
        password = pw.getpass("Password: ")
        conn = None
        conn = psycopg2.connect(host = "localhost", database = "postgres", user = username, password = password)
        return conn
    except Exception as e:
        print("Login information incorrect. Please restart and try again!")

# display menu function
def display_menu():
    print("\nMain Menu")
    print("1 - Enter Display Menu")
    print("2 - Enter Search Menu")
    print("3 - Enter Modify Menu (employees only)")
    print("4 - Exit")

# MAIN BEGINS HERE

conn = connection() # establish connection and ask for login info

if conn is None:
    print() # do nothing, connection wasn't estabished
else:
    display_menu()
    flag = True
    while flag:
        flag2 = input("\nEnter a command, or enter 0 to display main menu: ")
        print("\n")
        if flag2 == '1':
            displayFlag = True
            while(displayFlag):
                print("\nEntering Display Menu")
                print("1 - Display all games")
                print("2 - Display all companies")
                print("3 - Display all customers (employees only)")
                print("4 - Display all orders (employees only)")
                print("5 - Display all orders by ascending customer ID (employees only)")
                print("6 - Display all orders by ascending game ID (employees only)")
                displayinput = input("\nEnter a command or enter 0 to go back.\n")
                if displayinput == '1':
                    print("Displaying all games")
                    get_games(conn)
                elif displayinput == '2':
                    print("Displaying all companies")
                    get_companies(conn)
                elif displayinput == '3':
                    print("Displaying all customers")
                    get_customers(conn)
                elif displayinput == '4':
                    print("Displaying all orders")
                    get_orders(conn)
                elif displayinput == '5':
                    print("Displaying all orders by ascending customer ID")
                    get_sorted_orders_by_customer_id(conn)
                elif displayinput == '6':
                    print("Displaying all orders by ascending game ID")
                    get_sorted_orders_by_game_id(conn)
                elif displayinput == '0':
                    displayFlag = False
                else:
                    print("Invalid Command")
        elif flag2 == '2':
            searchFlag = True
            while(searchFlag):
                print("\nEntering Search Menu")
                print("1 - Search games by name")
                print("2 - Search games by genre")
                print("3 - Search games by company")
                print("4 - Search orders by customer ID (employees only)")
                print("5 - Search orders by game ID (employees only)")
                searchinput = input("\nEnter a command or enter 0 to go back.\n")
                if searchinput == '1':
                    print("Search games by name")
                    search_games_by_name(conn)
                elif searchinput == '2':
                    print("Search games by genre")
                    search_games_by_genre(conn)
                elif searchinput == '3':
                    print("Search games by company")
                    search_games_by_company(conn)
                elif searchinput == '4':
                    print("Search orders by customer ID")
                    search_orders_by_customer_id(conn)
                elif searchinput == '5':
                    print("Search orders by game ID")
                    search_orders_by_game_id(conn)
                elif searchinput == '0':
                    searchFlag = False
                else:
                    print("Invalid Command")
        elif flag2 == '3':
            modifyFlag = True
            while(modifyFlag):
                print("\nEntering Modify Menu (employees only)")
                print("1 - Add new game")
                print("2 - Add new company")
                print("3 - Add new customer")
                print("4 - Add new orders")
                print("5 - Delete game")
                print("6 - Delete company")
                print("7 - Delete customer")
                print("8 - Update price of game")
                print("9 - Create a new user account")
                print("10 - Delete a user account")
                modifyinput = input("\nEnter a command or enter 0 to go back.\n")
                if modifyinput == '1':
                    print("Adding new game")
                    add_new_game(conn)
                elif modifyinput == '2':
                    print("Adding new company")
                    add_new_company(conn)
                elif modifyinput == '3':
                    print("Adding new customer")
                    add_new_customer(conn)
                elif modifyinput == '4':
                    print("Adding new order")
                    add_new_order(conn)
                elif modifyinput == '5':
                    print("Deleting game")
                    delete_game(conn)
                elif modifyinput == '6':
                    print("Deleting company")
                    delete_company(conn)
                elif modifyinput == '7':
                    print("Deleting customer")
                    delete_customer(conn)
                elif modifyinput == '8':
                    print("Updating game")
                    update_game(conn)
                elif modifyinput == '9':
                    print("Creating a new user account")
                    create_new_user(conn)
                elif modifyinput == '10':
                    print("Deleting a user account")
                    delete_user(conn)
                elif modifyinput == '0':
                    modifyFlag = False
                else:
                    print("Invalid Command")
        elif flag2 == '4':
            print("Exiting database.")
            flag = False
        elif flag2 == '0':
            display_menu()
        else:
            print("Invalid command.")

    print("Goodbye!")
