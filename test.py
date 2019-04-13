import psycopg2
import psycopg2.extensions
import getpass as pw
import datetime

# print functions

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
    
# select all functions

def get_games(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Games";')
    rs = cur.fetchall()
    print_games(rs)
    cur.close()

def get_companies(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Company";')
    rs = cur.fetchall()
    print_companies(rs)
    cur.close()

def get_customers(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Customer";')
    rs = cur.fetchall()
    print_customers(rs)
    cur.close()

def get_orders(conn):

    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Orders";')
    rs = cur.fetchall()
    print_orders(rs)
    cur.close()

# search functions

def search_games_by_name(conn):
    search = input("Enter a name to search by: ")
    search = search.lower().strip()
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Games" WHERE LOWER("Title") LIKE \'%' + search + '%\';')
    rs = cur.fetchall()
    print_games(rs)
    cur.close()

def search_games_by_genre(conn):
    search = input("Enter a genre to search by: ")
    search = search.lower().strip()
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Games" WHERE LOWER("Genre") LIKE \'%' + search + '%\';')
    rs = cur.fetchall()
    print_games(rs)
    cur.close()

def search_games_by_company(conn):
    search = input("Enter a company (publisher) to search by: ")
    search = search.lower().strip()
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Games" WHERE LOWER("Publisher") LIKE \'%' + search + '%\';')
    rs = cur.fetchall()
    print_games(rs)
    cur.close()

# user functions
def create_new_user(conn):
    print("Creating a new user...")
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirmpass = input("Confirm password: ")
    key = input("Enter key (ignore if customer): ")
    if password != confirmpass:
        print("password does not match")
    elif password == confirmpass and key != '1234':
        print("create customer account")
        cur = conn.cursor()
        cur.execute("CREATE USER %s WITH PASSWORD '%s'" %(username, password)) 
        conn.commit()
    elif password == confirmpass and key == '1234':
        print("created employee account")
        cur = conn.cursor()
        cur.execute("CREATE USER %s WITH PASSWORD '%s'" %(username, password)) 
        conn.commit()
           
def connection():
    username = input("Enter Username: ")
    password = pw.getpass("Password: ")
    conn = None
    conn = psycopg2.connect(host = "localhost", database = "postgres", user = username, password = password)
    return conn

def display_menu():
    print("1 - Display all games")
    print("2 - Display all companies")
    print("3 - Display all customers")
    print("4 - Display all orders")
    print("5 - Search games by name")
    print("6 - Search games by genre")
    print("7 - Search games by company")
    print("8 - Add a new game")
    print("9 - Create new customer or employee account")
    print("10 - Exit")

conn = connection()
#create_new_user(conn)

display_menu()
flag = True
while flag:
    flag2 = input("Enter a command (or enter 0 to display menu): ")
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
        print("Add new game:")
        #add_new_game()
    elif flag2 == '9':
        print("Create new account:")
        #create_new_user()
    elif flag2 == '10':
        print("Exiting Database")
        flag = False
    else:
        print("Invalid command.")
conn.close()