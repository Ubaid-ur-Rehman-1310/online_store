import mysql.connector
from getpass import getpass
import datetime

# create a MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ubaid1999",
    database="online_store"
)
cursor = db.cursor()

def create_account():
    name = input('enter a username: ')
    email = input('enter an email: ')
    password = getpass('enter a password: ')
    password2 = getpass('confirm password: ')
    if password == password2:
        cursor.execute("INSERT INTO Users (user_name, user_email,user_password) VALUES (%s, %s, %s)", (name, email, password))
        db.commit()
        print('account created')
    else:
        print('passwords do not match')

def main():
    while True:
        print('\nMenu:')
        print("1. Create an Account")
        print("2. Browse Products")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Place Order")
        print("6. Exit")
        choice = input('Enter your choice: ')
        if choice == '1':
            create_account()
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

#Close the connection
db.close()
