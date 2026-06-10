# 📦 Inventory Management System

A comprehensive terminal-based Inventory Management System developed using **Python** and **SQLite**, designed to streamline inventory operations, supplier management, stock tracking, and reporting through a modular, object-oriented architecture.

This project demonstrates the practical implementation of **Python Programming**, **Object-Oriented Programming (OOP)**, **SQL Database Management**, and **Menu-Driven Application Development** in a real-world business scenario.

---

# 🚀 Project Highlights

✔ Secure Admin Authentication

✔ Product Management System

✔ Supplier Management System

✔ Inventory Tracking

✔ Stock In / Stock Out Operations

✔ Transaction Logging & History

✔ Low Stock Monitoring

✔ Dashboard & Reporting Module

✔ SQLite Relational Database

✔ Modular OOP-Based Design

✔ SQL JOIN-Based Data Retrieval

---

# 🎯 Problem Statement

Businesses need an efficient way to manage products, suppliers, and inventory levels while maintaining accurate transaction records.

Manual inventory management can result in:

* Stock shortages
* Overstocking
* Data inconsistencies
* Inefficient supplier tracking
* Lack of operational insights

This Inventory Management System provides a centralized solution to automate inventory operations and improve stock management efficiency.

---

# ✨ Features

### 📦 Product Management

* Add New Product
* View Products
* Search Product
* Update Product Details
* Delete Product
* Product Availability Check

### 🚚 Supplier Management

* Add Supplier
* View Suppliers
* Search Supplier
* Update Supplier Information
* Delete Supplier

### 📈 Inventory Tracking

* Stock In Operations
* Stock Out Operations
* Quantity Monitoring
* Inventory Movement Tracking
* Transaction History Management

### ⚠️ Low Stock Monitoring

* Detect Low Stock Products
* Reorder-Level Tracking
* Out-of-Stock Identification

### 📊 Reporting Module

* Dashboard Summary
* Inventory Report
* Low Stock Report
* Out of Stock Report
* Supplier Wise Report

### 🔐 Authentication

* Admin Login Validation
* Access Control Before System Usage

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

### OOP Concepts Applied

* Encapsulation
* Abstraction
* Modular Design
* Class-Based Programming
* Separation of Concerns

This modular architecture improves scalability, maintainability, and code readability.

---

# 🗄 Database Design

The application uses SQLite as the backend database and follows a relational database structure.

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
* Restricted Access for Authorized Users

---

## 📦 Product Management

* Create Products
* Update Product Information
* Delete Products
* Search Products
* View Product Inventory

---

## 🚚 Supplier Management

* Manage Supplier Information
* Associate Suppliers with Products
* Supplier Search and Updates

---

## 📈 Inventory Operations

### Stock In

Increases product quantity when new inventory arrives.

### Stock Out

Reduces product quantity when products are sold or issued.

### Inventory Tracking

Tracks stock movement and maintains inventory accuracy.

### Transaction Logging

Records every inventory operation for audit and reporting purposes.

---

## 📊 Reporting Module

### Dashboard Report

Provides an overview of:

* Total Products
* Total Suppliers
* Total Transactions
* Inventory Statistics

### Inventory Report

Displays all available inventory records.

### Low Stock Report

Lists products that require replenishment.

### Out of Stock Report

Identifies products with zero available quantity.

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

# 📸 Screenshots

Add screenshots of your application here.

### Login Screen

![Login](screenshots/login.png)

### Main Menu

![Main Menu](screenshots/main_menu.png)

### Product Management

![Products](screenshots/products.png)

### Reports Dashboard

![Reports](screenshots/reports.png)

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

### Run the Application

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
* CRUD Operations
* Transaction Processing
* Report Generation
* Inventory Tracking
* Menu-Driven Application Development

---

# 🌍 Real-World Relevance

This Inventory Management System can be adapted for:

* Retail Stores
* Warehouses
* Pharmacies
* Small Businesses
* Distribution Centers

The system helps organizations monitor stock levels, manage suppliers, track inventory movement, and generate operational reports efficiently.

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
