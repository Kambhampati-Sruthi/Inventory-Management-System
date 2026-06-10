import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("inventory.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS suppliers(
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            supplier_name TEXT NOT NULL,
            contact TEXT UNIQUE,
            email TEXT UNIQUE
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category TEXT,
            price REAL NOT NULL,
            quantity INTEGER DEFAULT 0,
            reorder_level INTEGER DEFAULT 10,
            supplier_id INTEGER,
            FOREIGN KEY(supplier_id)
            REFERENCES suppliers(supplier_id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            transaction_type TEXT,
            quantity INTEGER,
            remarks TEXT,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(product_id)
            REFERENCES products(product_id)
        )
        """)

        self.conn.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()