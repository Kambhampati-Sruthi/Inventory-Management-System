class Product:

    def __init__(self, db):
        self.db = db

    def add_product(self):

        try:
            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))
            reorder_level = int(input("Enter Reorder Level: "))
            supplier_id = int(input("Enter Supplier ID: "))

            query = """
            INSERT INTO products(
                product_name,
                category,
                price,
                quantity,
                reorder_level,
                supplier_id
            )
            VALUES(?,?,?,?,?,?)
            """

            self.db.execute(
                query,
                (
                    name,
                    category,
                    price,
                    quantity,
                    reorder_level,
                    supplier_id
                )
            )

            print("\n✅ Product Added Successfully\n")

        except Exception as e:
            print("Error:", e)

    def view_products(self):

        query = """
        SELECT
            p.product_id,
            p.product_name,
            p.category,
            p.price,
            p.quantity,
            p.reorder_level,
            s.supplier_name

        FROM products p

        LEFT JOIN suppliers s

        ON p.supplier_id = s.supplier_id
        """

        rows = self.db.fetchall(query)

        if not rows:
            print("\nNo Products Found\n")
            return

        print("\n===== PRODUCTS =====\n")

        for row in rows:
            print(row)

    def search_product(self):

        keyword = input("Enter Product Name: ")

        query = """
        SELECT *
        FROM products
        WHERE product_name LIKE ?
        """

        rows = self.db.fetchall(
            query,
            ('%' + keyword + '%',)
        )

        if not rows:
            print("No Product Found")
            return

        print("\n===== SEARCH RESULT =====\n")

        for row in rows:
            print(row)

    def update_product(self):

        try:
            product_id = int(input("Enter Product ID: "))

            row = self.db.fetchone(
                """
                SELECT *
                FROM products
                WHERE product_id=?
                """,
                (product_id,)
            )

            if not row:
                print("Product Not Found")
                return

            new_price = float(input("Enter New Price: "))
            new_quantity = int(input("Enter New Quantity: "))

            self.db.execute(
                """
                UPDATE products
                SET price=?,
                    quantity=?
                WHERE product_id=?
                """,
                (
                    new_price,
                    new_quantity,
                    product_id
                )
            )

            print("\n✅ Product Updated Successfully\n")

        except Exception as e:
            print("Error:", e)

    def delete_product(self):

        try:
            product_id = int(input("Enter Product ID: "))

            row = self.db.fetchone(
                """
                SELECT *
                FROM products
                WHERE product_id=?
                """,
                (product_id,)
            )

            if not row:
                print("Product Not Found")
                return

            self.db.execute(
                """
                DELETE FROM products
                WHERE product_id=?
                """,
                (product_id,)
            )

            print("\n✅ Product Deleted Successfully\n")

        except Exception as e:
            print("Error:", e)

    def low_stock_products(self):

        query = """
        SELECT
            product_id,
            product_name,
            quantity,
            reorder_level
        FROM products
        WHERE quantity <= reorder_level
        """

        rows = self.db.fetchall(query)

        print("\n===== LOW STOCK PRODUCTS =====\n")

        if not rows:
            print("No Low Stock Products")
            return

        for row in rows:
            print(row)