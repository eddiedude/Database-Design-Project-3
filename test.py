import psycopg2.extensions
import psycopg2
import getpass as pw


def get_games(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Games";',cur.rowcount)
    row = cur.fetchone()
    i = 0
    while row is not None:
        i += 1
        print(i, row)
        row = cur.fetchone()
    cur.close()

def get_companies(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Company";',cur.rowcount)
    row = cur.fetchone()

    i = 0
    while row is not None:
        i += 1
        print(i, row)
        row = cur.fetchone()
    cur.close()

def get_customers(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Customer";',cur.rowcount)
    row = cur.fetchone()

    i = 0
    while row is not None:
        i += 1
        print(i, row)
        row = cur.fetchone()
    cur.close()

def get_orders(conn):

    cur = conn.cursor()
    cur.execute('SELECT * FROM public."Orders";',cur.rowcount)
    row = cur.fetchone()
    i = 0
    while row is not None:
        i += 1
        print(i, row)
        row = cur.fetchone()
    cur.close()

def create_new_user(conn):
    
    username = input("Enter username:")
    password = input("Enter password:")
    confirmpass = input("Confirm password")
    key = input("Enter key(ignore if customer): ")
    if password == confirmpass and key != '1234':
        print("create customer account")
        #print("CREATE USER %s WITH LOGIN NOSUPERUSER NOCREATEDB CREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT-1 PASSWORD '%s'" %(username,password))
        cur = conn.cursor()
        cur.execute("CREATE USER %s WITH LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT-1 PASSWORD '%s'" %(username,password))    
    elif password == confirmpass and key == '1234':
        print("created employee account")
        #print("CREATE USER %s WITH LOGIN NOSUPERUSER NOCREATEDB CREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT-1 PASSWORD '%s'" %(username,password))
        cur = conn.cursor()
        cur.execute("CREATE USER %s WITH LOGIN NOSUPERUSER NOCREATEDB CREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT-1 PASSWORD '%s'" %(username,password))
    elif password != confirmpass:
        print("password does not match")

        


def connection():
    #username = input("Enter Username: ")
    #password = pw.getpass("Password:")
    conn = None
    conn = psycopg2.connect(host = "localhost", database = "postgres", user = 'postgres', password = 'lech4se2')
    return conn


conn = connection()
create_new_user(conn)

print("1 - Display all Games")
print("2 - Display all Companies")
print("3 - Display all Customers")
print("4 - Display all Orders")
print("9 - Exit")
flag = True
while flag:
    flag2 = input("Enter a command: ")
    print("\n")
    if flag2 == '1':
        print("Games:")
        get_games(conn)
    elif flag2 == '2':
        print("Comapnies")
        get_companies(conn)
    elif flag2 == '3':
        print("Customers:")
        get_customers(conn)
    elif flag2 == '4':
        print("Orders:")
        get_orders(conn)
    elif flag2 == '9':
        print("Exiting Database")
        flag = False
    else:
        print("Invalid command.")
