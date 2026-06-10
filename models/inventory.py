class Inventory:

    def __init__(self, db):
        self.db = db

    def stock_in(self):

        try:
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity To Add: "))

            product = self.db.fetchone(
                """
                SELECT quantity
                FROM products
                WHERE product_id=?
                """,
                (product_id,)
            )

            if not product:
                print("Product Not Found")
                return

            self.db.execute(
                """
                UPDATE products
                SET quantity = quantity + ?
                WHERE product_id = ?
                """,
                (
                    quantity,
                    product_id
                )
            )

            self.db.execute(
                """
                INSERT INTO transactions(
                    product_id,
                    transaction_type,
                    quantity,
                    remarks
                )
                VALUES(?,?,?,?)
                """,
                (
                    product_id,
                    "STOCK_IN",
                    quantity,
                    "Inventory Added"
                )
            )

            print("\n✅ Stock Added Successfully\n")

        except Exception as e:
            print("Error:", e)

    def stock_out(self):

        try:
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity To Remove: "))

            product = self.db.fetchone(
                """
                SELECT quantity
                FROM products
                WHERE product_id=?
                """,
                (product_id,)
            )

            if not product:
                print("Product Not Found")
                return

            current_stock = product[0]

            if current_stock < quantity:
                print("\n❌ Insufficient Stock Available\n")
                return

            self.db.execute(
                """
                UPDATE products
                SET quantity = quantity - ?
                WHERE product_id = ?
                """,
                (
                    quantity,
                    product_id
                )
            )

            self.db.execute(
                """
                INSERT INTO transactions(
                    product_id,
                    transaction_type,
                    quantity,
                    remarks
                )
                VALUES(?,?,?,?)
                """,
                (
                    product_id,
                    "STOCK_OUT",
                    quantity,
                    "Inventory Removed"
                )
            )

            print("\n✅ Stock Removed Successfully\n")

        except Exception as e:
            print("Error:", e)

    def check_quantity(self):

        try:
            product_id = int(input("Enter Product ID: "))

            row = self.db.fetchone(
                """
                SELECT
                    product_name,
                    quantity
                FROM products
                WHERE product_id=?
                """,
                (product_id,)
            )

            if not row:
                print("Product Not Found")
                return

            print("\n===== PRODUCT STOCK =====")
            print(f"Product Name : {row[0]}")
            print(f"Quantity     : {row[1]}")

        except Exception as e:
            print("Error:", e)

    def product_availability(self):

        try:
            product_id = int(input("Enter Product ID: "))

            row = self.db.fetchone(
                """
                SELECT
                    product_name,
                    quantity
                FROM products
                WHERE product_id=?
                """,
                (product_id,)
            )

            if not row:
                print("Product Not Found")
                return

            if row[1] > 0:
                print(f"\n✅ {row[0]} is Available")
            else:
                print(f"\n❌ {row[0]} is Out Of Stock")

        except Exception as e:
            print("Error:", e)

    def transaction_history(self):

        rows = self.db.fetchall(
            """
            SELECT *
            FROM transactions
            ORDER BY transaction_date DESC
            """
        )

        print("\n===== TRANSACTION HISTORY =====\n")

        if not rows:
            print("No Transactions Found")
            return

        for row in rows:
            print(row)