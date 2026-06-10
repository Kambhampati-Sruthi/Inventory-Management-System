# 📦 Inventory Management System

A comprehensive terminal-based Inventory Management System developed using **Python** and **SQLite**, designed to streamline inventory operations, supplier management, stock tracking, and reporting through a modular, object-oriented architecture.

This project demonstrates the practical implementation of **Python programming**, **Object-Oriented Programming (OOP)**, **SQL database management**, and **menu-driven application development** in a real-world business scenario.

---

# 🚀 Project Highlights

✔ Secure Admin Authentication

✔ Product Management System

✔ Supplier Management System

✔ Inventory Stock Tracking

✔ Stock In / Stock Out Operations

✔ Transaction Logging & History

✔ Low Stock Monitoring

✔ Dashboard & Reporting Module

✔ SQLite Relational Database

✔ Modular OOP-Based Design

✔ SQL JOIN-Based Data Retrieval

---

# 🎯 Problem Statement

Managing inventory manually can lead to inaccurate stock records, supplier tracking issues, and inefficient reporting.

This Inventory Management System addresses these challenges by providing a centralized solution for:

* Product Management
* Supplier Management
* Inventory Monitoring
* Transaction Tracking
* Operational Reporting

---

# 🛠 Technologies Used

| Technology         | Purpose                       |
| ------------------ | ----------------------------- |
| Python             | Core Application Development  |
| SQLite             | Database Management           |
| SQL                | Data Manipulation & Retrieval |
| OOP                | Modular Software Design       |
| Terminal Interface | User Interaction              |

---

# 🏗 System Architecture

```text
Inventory-Management-System
│
├── main.py
├── auth.py
├── database.py
│
├── models
│   ├── product.py
│   ├── supplier.py
│   └── inventory.py
│
├── reports
│   └── reports.py
│
└── inventory.db
```

---

# 📚 Object-Oriented Design

The project follows Object-Oriented Programming principles by separating responsibilities into dedicated classes.

| Class     | Responsibility                        |
| --------- | ------------------------------------- |
| Database  | Database Connection & Query Execution |
| Auth      | User Authentication                   |
| Product   | Product Operations                    |
| Supplier  | Supplier Operations                   |
| Inventory | Inventory Transactions                |
| Reports   | Analytics & Reporting                 |

This modular structure improves maintainability, scalability, and code readability.

---

# 🗄 Database Design

The system uses SQLite as the backend database and follows a normalized relational schema.

## Suppliers Table

| Field         | Type         |
| ------------- | ------------ |
| supplier_id   | INTEGER (PK) |
| supplier_name | TEXT         |
| contact       | TEXT         |
| email         | TEXT         |

---

## Products Table

| Field         | Type         |
| ------------- | ------------ |
| product_id    | INTEGER (PK) |
| product_name  | TEXT         |
| category      | TEXT         |
| price         | REAL         |
| quantity      | INTEGER      |
| reorder_level | INTEGER      |
| supplier_id   | INTEGER (FK) |

---

## Transactions Table

| Field            | Type         |
| ---------------- | ------------ |
| transaction_id   | INTEGER (PK) |
| product_id       | INTEGER (FK) |
| transaction_type | TEXT         |
| quantity         | INTEGER      |
| remarks          | TEXT         |
| transaction_date | TIMESTAMP    |

---

# ⚙ Key Functionalities

## 🔐 Authentication Module

* Admin Login Validation
* Access Control Before System Usage

---

## 📦 Product Management

* Add New Product
* View Products
* Search Product
* Update Product Details
* Delete Product
* Identify Low Stock Products

---

## 🚚 Supplier Management

* Add Supplier
* View Supplier Information
* Search Supplier
* Update Supplier Details
* Delete Supplier

---

## 📈 Inventory Operations

### Stock In

Increase available inventory when new stock arrives.

### Stock Out

Reduce inventory when products are issued or sold.

### Quantity Verification

Check current stock availability instantly.

### Product Availability

Verify inventory status before operations.

### Transaction Tracking

Maintain a complete history of stock movements.

---

## 📊 Reporting Module

### Dashboard

Provides an overview of:

* Total Products
* Total Suppliers
* Total Transactions
* Inventory Statistics

### Inventory Report

Displays complete inventory information.

### Low Stock Report

Identifies products that require replenishment.

### Out of Stock Report

Highlights unavailable products.

### Supplier Wise Report

Displays products grouped by supplier using SQL JOIN operations.

---

# 💡 SQL Concepts Demonstrated

The project showcases practical SQL implementation including:

* CREATE TABLE
* INSERT
* SELECT
* UPDATE
* DELETE
* WHERE Clause
* Aggregate Queries
* COUNT()
* INNER JOIN
* Foreign Keys
* Relational Database Design

---

# 🔄 System Workflow

```text
Login
   ↓
Main Menu
   ↓
 ┌──────────────────────┐
 │ Product Management   │
 │ Supplier Management  │
 │ Inventory Operations │
 │ Reports              │
 └──────────────────────┘
   ↓
Database Operations
   ↓
Reports & Analytics
```

---

# ▶ How to Run

### Clone Repository

```bash
git clone https://github.com/Kambhampati-Sruthi/Inventory-Management-System.git
```

### Navigate to Project Folder

```bash
cd Inventory-Management-System
```

### Execute Application

```bash
python main.py
```

---

# 📖 Learning Outcomes

Through this project, the following concepts were implemented and reinforced:

* Python Programming Fundamentals
* Object-Oriented Programming
* Database Connectivity
* SQLite Database Management
* SQL Query Writing
* Modular Software Design
* CRUD Operations
* Transaction Management
* Report Generation
* Menu-Driven Application Development

---

# 🔮 Future Enhancements

* Password Encryption
* Role-Based Access Control
* CSV Export Functionality
* Inventory Value Analytics
* Barcode Integration
* GUI-Based Interface
* Web-Based Deployment

---

