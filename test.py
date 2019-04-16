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

        gid = gid.strip();
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

'''
to drop a user after granting them privileges:
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM hello;
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM hello;
REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM hello;
DROP USER hello;
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
    print("1 - Display all games")
    print("2 - Display all companies")
    print("3 - Display all customers")
    print("4 - Display all orders")
    print("5 - Search games by name")
    print("6 - Search games by genre")
    print("7 - Search games by company")
    print("8 - Add a new game")
    print("9 - Add a new company")
    print("10 - Add a new customer")
    print("11 - Add a new order")
    print("12 - Create new customer or employee account")
    print("99 - Exit")

# MAIN BEGINS HERE

conn = connection() # establish connection and ask for login info

if conn is None:
    print() # do nothing, connection wasn't estabished
else:
    display_menu()
    flag = True
    while flag:
        flag2 = input("\nEnter a command, or enter 0 to display menu: ")
        print("\n")
        if flag2 == '0':
            display_menu()
        elif flag2 == '1':
            print("Games:")
            get_games(conn)
        elif flag2 == '2':
            print("Companies:")
            get_companies(conn)
        elif flag2 == '3':
            print("Customers:")
            get_customers(conn)
        elif flag2 == '4':
            print("Orders:")
            get_orders(conn)
        elif flag2 == '5':
            print("Search games by name:")
            search_games_by_name(conn)
        elif flag2 == '6':
            print("Search games by genre:")
            search_games_by_genre(conn)
        elif flag2 == '7':
            print("Search games by company:")
            search_games_by_company(conn)
        elif flag2 == '8':
            print("Add a new game:")
            add_new_game(conn)
        elif flag2 == '9':
            print("Add a new company:")
            add_new_company(conn)
        elif flag2 == '10':
            print("Add a new customer:")
            add_new_customer(conn)
        elif flag2 == '11':
            print("Add a new order:")
            add_new_order(conn)
        elif flag2 == '12':
            print("Create a new user account:")
            create_new_user(conn)
        elif flag2 == '99':
            print("Exiting database.")
            flag = False
        else:
            print("Invalid command.")
    conn.close()
print("Goodbye!")