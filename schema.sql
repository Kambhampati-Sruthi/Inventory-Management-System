-- Suppliers Table

CREATE TABLE suppliers (
supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
supplier_name TEXT NOT NULL,
contact TEXT,
email TEXT
);

-- Products Table

CREATE TABLE products (
product_id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name TEXT NOT NULL,
category TEXT,
price REAL,
quantity INTEGER,
reorder_level INTEGER,
supplier_id INTEGER,
FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Transactions Table

CREATE TABLE transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
product_id INTEGER,
transaction_type TEXT,
quantity INTEGER,
remarks TEXT,
transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (product_id) REFERENCES products(product_id)
);
