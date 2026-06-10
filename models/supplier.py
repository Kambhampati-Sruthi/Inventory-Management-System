class Supplier:

    def __init__(self, db):
        self.db = db

    def add_supplier(self):

        try:
            supplier_name = input("Enter Supplier Name: ")
            contact = input("Enter Contact Number: ")
            email = input("Enter Email: ")

            query = """
            INSERT INTO suppliers(
                supplier_name,
                contact,
                email
            )
            VALUES(?,?,?)
            """

            self.db.execute(
                query,
                (
                    supplier_name,
                    contact,
                    email
                )
            )

            print("\n✅ Supplier Added Successfully\n")

        except Exception as e:
            print("Error:", e)

    def view_suppliers(self):

        query = """
        SELECT *
        FROM suppliers
        """

        rows = self.db.fetchall(query)

        if not rows:
            print("\nNo Suppliers Found\n")
            return

        print("\n===== SUPPLIERS =====\n")

        for row in rows:
            print(row)

    def search_supplier(self):

        keyword = input("Enter Supplier Name: ")

        query = """
        SELECT *
        FROM suppliers
        WHERE supplier_name LIKE ?
        """

        rows = self.db.fetchall(
            query,
            ('%' + keyword + '%',)
        )

        if not rows:
            print("Supplier Not Found")
            return

        print("\n===== SEARCH RESULT =====\n")

        for row in rows:
            print(row)

    def update_supplier(self):

        try:
            supplier_id = int(input("Enter Supplier ID: "))

            supplier = self.db.fetchone(
                """
                SELECT *
                FROM suppliers
                WHERE supplier_id=?
                """,
                (supplier_id,)
            )

            if not supplier:
                print("Supplier Not Found")
                return

            new_contact = input("Enter New Contact: ")
            new_email = input("Enter New Email: ")

            self.db.execute(
                """
                UPDATE suppliers
                SET contact=?,
                    email=?
                WHERE supplier_id=?
                """,
                (
                    new_contact,
                    new_email,
                    supplier_id
                )
            )

            print("\n✅ Supplier Updated Successfully\n")

        except Exception as e:
            print("Error:", e)

    def delete_supplier(self):

        try:
            supplier_id = int(input("Enter Supplier ID: "))

            supplier = self.db.fetchone(
                """
                SELECT *
                FROM suppliers
                WHERE supplier_id=?
                """,
                (supplier_id,)
            )

            if not supplier:
                print("Supplier Not Found")
                return

            products = self.db.fetchone(
                """
                SELECT *
                FROM products
                WHERE supplier_id=?
                """,
                (supplier_id,)
            )

            if products:
                print(
                    "Cannot delete supplier. Products are linked to this supplier."
                )
                return

            self.db.execute(
                """
                DELETE FROM suppliers
                WHERE supplier_id=?
                """,
                (supplier_id,)
            )

            print("\n✅ Supplier Deleted Successfully\n")

        except Exception as e:
            print("Error:", e)