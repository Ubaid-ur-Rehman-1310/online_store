import mysql.connector

# Establishing a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ubaid1999",
    database="online_store"
)

# Creating a cursor to execute SQL queries
cursor = db_connection.cursor()

# ... (Table creation queries are the same as before)

# Function to create a user account and retrieve the user ID
def create_account():
    global user_id
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input('enter a password: ')
    password2 = input('confirm password: ')
    if password == password2:
        insert_user_query = "INSERT INTO user (password,user_name, email) VALUES (%s,%s,%s)"
        cursor.execute(insert_user_query, (password,username, email))
        db_connection.commit()
        print("\nAccount created successfully!")
    else:
        print('\npasswords do not match')
        return None
    # Retrieve the user ID
    select_user_id_query = "SELECT user_id FROM user WHERE email = %s"
    cursor.execute(select_user_id_query, (email,))
    user_id = cursor.fetchone()[0]

    return user_id
# Function to login
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if the user exists
    select_user_query = "SELECT user_id, password FROM user WHERE email = %s"
    cursor.execute(select_user_query, (email,))
    result = cursor.fetchone()

    if result:
        stored_password = result[1]

        # Check if the entered password matches the stored hashed password
        if password == stored_password:
            print("\nLogin successful!")
            return result[0]
        else:
            print("\nInvalid password. Please try again.")
            return None
    else:
        print("\nUser not found. Please create an account.")
        return None

# Function to browse products
def browse_products():
    select_products_query = "SELECT * FROM product"
    cursor.execute(select_products_query)
    products = cursor.fetchall()

    print("Available Products:")
    for product in products:
        print(f"{product[0]}. {product[1]} - ${product[2]}")
# Function to add an item to the cart
def add_to_cart(user_id):
    if user_id is None:
        print("\nPlease create an account or login first.")
        return

    product_id = int(input("Enter the product ID you want to add to the cart: "))
    quantity = int(input("Enter the quantity: "))

    insert_cart_item_query = "INSERT INTO cart_item (user_id, product_id, quantity) VALUES (%s, %s, %s)"
    cursor.execute(insert_cart_item_query, (user_id, product_id, quantity))
    db_connection.commit()
    print("\nItem added to the cart successfully!")
 # Function to view the cart
def view_cart(user_id):
    if user_id is None:
        print("\nPlease create an account or login first.")
        return

    select_cart_query = """
    SELECT ci.cart_item_id, p.name, p.price, ci.quantity
    FROM cart_item ci
    JOIN product p ON ci.product_id = p.product_id
    WHERE ci.user_id = %s
    """
    cursor.execute(select_cart_query, (user_id,))
    cart_items = cursor.fetchall()

    if not cart_items:
        print("\nCart is empty.")
    else:
        print("\nYour Cart:")
        for item in cart_items:
            print(f"{item[1]} - ${item[2]} - Quantity: {item[3]}")
  # Function to place an order
# Function to place an order
def place_order(user_id):
    if user_id is None:
        print("\nPlease create an account or login first.")
        return

    view_cart(user_id)

    # Check if the cart is empty
    check_cart_query = "SELECT COUNT(*) FROM cart_item WHERE user_id = %s"
    cursor.execute(check_cart_query, (user_id,))
    cart_count = cursor.fetchone()[0]

    if cart_count == 0:
        print("You have nothing in your cart. Add items to your cart before placing an order.")
        return

    confirm = input("\nDo you want to place the order? (yes/no): ").lower()

    if confirm == "yes":
        # Calculate total amount from the cart
        select_cart_total_query = """
        SELECT SUM(p.price * ci.quantity) as total_amount
        FROM cart_item ci
        JOIN product p ON ci.product_id = p.product_id
        WHERE ci.user_id = %s
        """
        cursor.execute(select_cart_total_query, (user_id,))
        total_amount = cursor.fetchone()[0]

        # Get product ID and quantity from the cart
        select_cart_items_query = "SELECT product_id, quantity FROM cart_item WHERE user_id = %s"
        cursor.execute(select_cart_items_query, (user_id,))
        cart_items = cursor.fetchall()

        # Insert order into the orders table
        insert_order_query = """
        INSERT INTO orders (user_id, product_id, quantity,total_amount)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_order_query, (user_id, cart_items[0][0], cart_items[0][1], total_amount))

        # Clear the cart by deleting cart items
        delete_cart_items_query = "DELETE FROM cart_item WHERE user_id = %s"
        cursor.execute(delete_cart_items_query, (user_id,))

        db_connection.commit()
        print("\nOrder placed successfully!")
    else:
        # Clear the cart by deleting cart items
        delete_cart_items_query = "DELETE FROM cart_item WHERE user_id = %s"
        cursor.execute(delete_cart_items_query, (user_id,))
        print("\nOrder canceled.")

 
def main():
    user_id = None
    
    while True:
        print('\nMenu:')
        print("1. Create an Account")
        print("2. Log In")
        print("3. Browse Products")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Place Order")
        print("7. Exit")
        choice = int(input('Enter your choice: '))
        if choice == 1:
            user_id = create_account()
        elif choice == 2:
            user_id = login()
        elif choice == 3:
            browse_products()
        elif choice == 4:
            add_to_cart(user_id)
        elif choice == 5:
            view_cart(user_id)
        elif choice == 6:
            place_order(user_id)
        elif choice == 7:
            print('Goodbye!')
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()