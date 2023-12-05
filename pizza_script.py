from multiprocessing import connection
from random import choice
from sqlite3 import Cursor
import mariadb
import sys
from prettytable import PrettyTable

# Function to establish a MariaDB connection
def connect_to_database():
    try:
        con = mysql.connector.connect(
            user='root',
            password='sat3210',
            host='localhost',
            port=3306 ,
            database='pizza'
        )
        return con
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

# Function to update two sets of information within database
def update_data(con, order_ID, cus_name, payment_type):
    try:
        cursor = con.cursor()
        query = "UPDATE customer_info SET cus_name=%s, payment_type=%s WHERE order_ID=%s"
        cursor.execute(query, (cus_name, payment_type, order_ID))
        con.commit()
        print("Data updated successfully.")
    except Exception as e:
        print("Error updating data:", e)

# Function to insert one set of information within database
def insert_data(con, points, discount, cus_name):
    try:
        cursor = con.cursor()
        query = "INSERT INTO rewards (points, discount, cus_name) VALUES %d,%d,%s"
        cursor.execute(query, (points, discount, cus_name))
        con.commit()
        print("Data updated successfully.")
    except Exception as e:
        print("Error updating data:", e)

# Function to delete one set of information within database
def delete_data(con, ID, item_ID):
    try:
        cursor = con.cursor()
        query = "DELETE FROM order_items WHERE ID = %d AND item_ID = %d"
        cursor.execute(query, (ID, item_ID))
        con.commit()
        print("Data updated successfully.")
    except Exception as e:
        print("Error updating data:", e)

# Function to display(#1) : 3 different forms of data within database
def display_data_1(con):
    try:
        cursor = con.cursor()
        query = "SELECT item_ID, item, item_price FROM menu LIMIT 10"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Displaying top 10 items on the menu:")
        table = PrettyTable(["item_id","item","item_price"])
        for row in rows:
            table.add_rows(row)
        print("Data updated successfully.")
    except Exception as e:
        print("Error updating data:", e)

# Function to display(#2) : 3 different forms of data within database
def display_data_2(con):
    try:
        cursor = con.cursor()
        query = "SELECT order_ID, total_cost, ID FROM receipt LIMIT 10"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Displaying 10 most recent receipts:")
        table = PrettyTable(["order_ID","total_cost","ID"])
        for row in rows:
            table.add_rows(row)
        print("Data updated successfully.")
    except Exception as e:
        print("Error updating data:", e)

# Function to display(#3) : 3 different forms of data within database
def display_data_3(con):
    try:
        cursor = con.cursor()
        query = "SELECT ID, name, salary FROM employee_info LIMIT 10"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("10 employess that work at pizza hut:")
        table = PrettyTable(["ID","name","salary"])
        for row in rows:
            table.add_rows(row)
        print("Data updated successfully.")
    except Exception as e:
        print("Error updating data:", e)

# Function to for exiting database conneciton
    if __name__ == '__main__':
        connection = connect_to_database()
        if connection is None:
            exit()

# Function to for user to interact with API
    while True:
        print("Options:")
        print("1. Update data")
        print("2. Insert new data")
        print("3. Delete data")
        print("4. Display data (option 1)")
        print("5. Display data (option 2)")
        print("6. Display data (option 3)")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            order_ID = int(input("Enter the order ID to update: "))
            cus_name = input("Enter your name: ")
            payment_type = input("'Cash' or 'Card'")
            update_data(connection, order_ID, cus_name, payment_type)
        elif choice == '2':
            points = int(input("Enter amount of points you have: "))
            discount = int(input("Enter discount [EX. 80% = .20]: "))
            cus_name = input("Enter your name: ")
            insert_data(connection, points, discount, cus_name)
        elif choice == '3':
            ID = int(input("Enter your ID number: "))
            item_ID = int(input("Enter the items ID number: "))
            delete_data(connection, ID, item_ID)
        elif choice == '4':
            display_data_1(connection)
        elif choice == '5':
            display_data_2(connection)
        elif choice == '6':
            display_data_3(connection)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    connection.close()