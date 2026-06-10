class Reports:

    def __init__(self, db):
        self.db = db

    def inventory_report(self):

        query = """
        SELECT
            p.product_id,
            p.product_name,
            p.category,
            p.price,
            p.quantity,
            s.supplier_name

        FROM products p

        LEFT JOIN suppliers s

        ON p.supplier_id = s.supplier_id

        ORDER BY p.product_id
        """

        rows = self.db.fetchall(query)

        print("\n" + "=" * 80)
        print("INVENTORY REPORT")
        print("=" * 80)

        if not rows:
            print("No Products Found")
            return

        for row in rows:
            print(row)

    def low_stock_report(self):

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

        print("\n" + "=" * 80)
        print("LOW STOCK REPORT")
        print("=" * 80)

        if not rows:
            print("No Low Stock Products")
            return

        for row in rows:
            print(row)

    def out_of_stock_report(self):

        query = """
        SELECT
            product_id,
            product_name,
            quantity

        FROM products

        WHERE quantity = 0
        """

        rows = self.db.fetchall(query)

        print("\n" + "=" * 80)
        print("OUT OF STOCK REPORT")
        print("=" * 80)

        if not rows:
            print("No Out Of Stock Products")
            return

        for row in rows:
            print(row)

    def supplier_wise_report(self):

        supplier_id = int(input("Enter Supplier ID: "))

        query = """
        SELECT
            p.product_id,
            p.product_name,
            p.category,
            p.quantity,
            s.supplier_name

        FROM products p

        JOIN suppliers s

        ON p.supplier_id = s.supplier_id

        WHERE s.supplier_id = ?
        """

        rows = self.db.fetchall(
            query,
            (supplier_id,)
        )

        print("\n" + "=" * 80)
        print("SUPPLIER WISE REPORT")
        print("=" * 80)

        if not rows:
            print("No Products Found")
            return

        for row in rows:
            print(row)

    def dashboard(self):

        total_products = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM products
            """
        )[0]

        total_suppliers = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM suppliers
            """
        )[0]

        total_transactions = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM transactions
            """
        )[0]

        low_stock = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM products
            WHERE quantity <= reorder_level
            """
        )[0]

        out_of_stock = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM products
            WHERE quantity = 0
            """
        )[0]

        print("\n" + "=" * 80)
        print("DASHBOARD")
        print("=" * 80)

        print(f"Total Products      : {total_products}")
        print(f"Total Suppliers     : {total_suppliers}")
        print(f"Total Transactions  : {total_transactions}")
        print(f"Low Stock Products  : {low_stock}")
        print(f"Out Of Stock Items  : {out_of_stock}")