# Online Store

This is a simple Python project for an online store using a MySQL database.

## Requirements

1. Python 3.x
   - Ensure compatibility with Python 3 and newer.
2. MySQL Connector for Python
   - Install the `mysql-connector-python` library using:
     ```bash
     pip install mysql-connector-python
     ```

## Project Overview

The project consists of a Python script (`online_store.py`) for an Online Store Management System. Users can create accounts, browse products, manage a shopping cart, and place orders. The MySQL database stores user information, product details, cart items, and order information.

## Database Setup

1. **MySQL Database:**
   - Install and configure a MySQL database server.
   - Create a database named `online_store`.
2. **Database Connection Parameters:**
   - Modify the script's database connection parameters (host, user, password) to match your MySQL configuration.
3. **Create Tables:**
   - Run the script to create tables (`user`, `product`, `cart_item`, `cart`, and `orders`) in the `online_store` database.

## Running the Program

1. **Execute the Main Script:**
   - Run `online_store.py` to launch the Online Store Management System.
2. **Menu Options:**
   - The program displays options for account creation, login, product browsing, cart management, order placement, and exit.
3. **Interact with the System:**
   - Follow on-screen prompts to navigate through the system features.

## Features

1. **Account Creation and Login:**
   - Users can create accounts and log in using email and password.
2. **Product Browsing:**
   - Users can view a list of available products.
3. **Shopping Cart Management:**
   - Users can add products to their cart.
4. **Viewing the Cart:**
   - Users can check the contents of their cart.
5. **Order Placement:**
   - Users can place orders, and the system calculates the total amount.

## Database Schema

- Tables: `user`, `product`, `cart_item`, `cart`, `orders`.

## Sample Data

- Sample product data is inserted into the `product` table.

## Note

- Customize the code as needed for additional features or improvements.
