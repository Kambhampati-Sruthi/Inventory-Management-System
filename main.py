from database import Database

from models.product import Product
from models.supplier import Supplier
from models.inventory import Inventory

from reports.reports import Reports

from auth import Auth


def product_menu(product):

    while True:

        print("\n" + "=" * 50)
        print("PRODUCT MANAGEMENT")
        print("=" * 50)

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Low Stock Products")
        print("7. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            product.add_product()

        elif choice == "2":
            product.view_products()

        elif choice == "3":
            product.search_product()

        elif choice == "4":
            product.update_product()

        elif choice == "5":
            product.delete_product()

        elif choice == "6":
            product.low_stock_products()

        elif choice == "7":
            break

        else:
            print("Invalid Choice")


def supplier_menu(supplier):

    while True:

        print("\n" + "=" * 50)
        print("SUPPLIER MANAGEMENT")
        print("=" * 50)

        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Search Supplier")
        print("4. Update Supplier")
        print("5. Delete Supplier")
        print("6. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            supplier.add_supplier()

        elif choice == "2":
            supplier.view_suppliers()

        elif choice == "3":
            supplier.search_supplier()

        elif choice == "4":
            supplier.update_supplier()

        elif choice == "5":
            supplier.delete_supplier()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")


def inventory_menu(inventory):

    while True:

        print("\n" + "=" * 50)
        print("INVENTORY OPERATIONS")
        print("=" * 50)

        print("1. Stock In")
        print("2. Stock Out")
        print("3. Check Quantity")
        print("4. Product Availability")
        print("5. Transaction History")
        print("6. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            inventory.stock_in()

        elif choice == "2":
            inventory.stock_out()

        elif choice == "3":
            inventory.check_quantity()

        elif choice == "4":
            inventory.product_availability()

        elif choice == "5":
            inventory.transaction_history()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")


def report_menu(report):

    while True:

        print("\n" + "=" * 50)
        print("REPORTS")
        print("=" * 50)

        print("1. Dashboard")
        print("2. Inventory Report")
        print("3. Low Stock Report")
        print("4. Out Of Stock Report")
        print("5. Supplier Wise Report")
        print("6. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            report.dashboard()

        elif choice == "2":
            report.inventory_report()

        elif choice == "3":
            report.low_stock_report()

        elif choice == "4":
            report.out_of_stock_report()

        elif choice == "5":
            report.supplier_wise_report()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")


def main():

    auth = Auth()

    if not auth.login():
        print("\nAccess Denied")
        return

    db = Database()

    db.create_tables()

    product = Product(db)
    supplier = Supplier(db)
    inventory = Inventory(db)
    report = Reports(db)

    while True:

        print("\n" + "=" * 60)
        print("INVENTORY MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1. Product Management")
        print("2. Supplier Management")
        print("3. Inventory Operations")
        print("4. Reports")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            product_menu(product)

        elif choice == "2":
            supplier_menu(supplier)

        elif choice == "3":
            inventory_menu(inventory)

        elif choice == "4":
            report_menu(report)

        elif choice == "5":
            print("\nThank You For Using Inventory Management System")
            db.close()
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()