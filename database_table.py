# connect to database
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ubaid1999",
    database="online_store"
)

cursor = db.cursor()

# create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_price DECIMAL(10,2) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_password VARCHAR(225) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cart_items (
    cart_item_id INT AUTO_INCREMENT PRIMARY KEY,
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
)
""")

 #insert sample data for products
data_to_insert = [
    ('Laptop', 999.99),
    ('Smartphone', 499.99),
    ('Tablet', 299.99),
    ('Headphones', 79.99),
    ('Digital Camera', 349.99),
    ('Wireless Mouse', 29.99),
    ('External Hard Drive', 129.99),
    ('Printer', 199.99),
    ('Fitness Tracker', 69.99),
    ('Bluetooth Speaker', 89.99),
    ('Gaming Laptop', 1499.99),
    ('Smartwatch', 199.99),
    ('E-book Reader', 79.99),
    ('Noise-Canceling Headphones', 149.99),
    ('Mirrorless Camera', 799.99),
    ('Mechanical Keyboard', 99.99),
    ('Portable SSD', 159.99),
    ('All-in-One Printer', 299.99),
    ('Activity Tracker', 49.99),
    ('Wireless Earbuds', 129.99)
 ]

cursor.executemany("INSERT INTO Products (product_name, product_price) VALUES (%s, %s)", data_to_insert)
print('Inserted products into the database')
db.commit()


