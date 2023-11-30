# connect to database
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ubaid1999",
    database="online_store"
)

cursor = db.cursor()

# create tables

create_user_table = """
CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""

create_product_table = """
CREATE TABLE IF NOT EXISTS product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
)
"""

create_cart_item_table = """
CREATE TABLE IF NOT EXISTS cart_item (
    cart_item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
)
"""

create_cart_table = """
CREATE TABLE IF NOT EXISTS cart (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
)
"""

create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10, 2),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
)
"""
# # Execute table creation queries
cursor.execute(create_user_table)
cursor.execute(create_product_table)
cursor.execute(create_cart_item_table)
cursor.execute(create_cart_table)
cursor.execute(create_orders_table)
# # Committing the changes
db.commit()
# insert sample data for products
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
cursor.executemany("INSERT INTO product (name, price) VALUES (%s, %s)", data_to_insert)
print('Inserted products into the database')
db.commit()