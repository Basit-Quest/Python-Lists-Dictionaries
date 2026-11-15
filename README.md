# Smart Grocery Store Management System

A beginner-friendly, menu-driven **Python command-line application** for managing a small grocery store's products, stock, sales, and daily sales summary.

This project demonstrates **lists, dictionaries, functions, loops, conditional statements, input validation, and formatted output**.

## Features

| Menu Option | Feature | Description |
|---|---|---|
| 1 | Add New Product | Add a product with a unique numeric ID, name, category, price, and stock quantity. |
| 2 | View All Products | See the complete product inventory in a table. |
| 3 | Search Product | Search by product ID or by all or part of a name (case-insensitive). |
| 4 | Update Product Stock | Add to an existing stock quantity or replace it with a new quantity. |
| 5 | Process Customer Sale | Validate the requested quantity, calculate the bill, deduct stock, and record a completed sale. |
| 6 | View Sales Records | Display completed transactions and their totals. |
| 7 | Generate Store Report | Show inventory statistics, sales, revenue, low-stock items, and price extremes. |
| 8 | Exit | Close the application. |

## Requirements

- **Python 3.8 or newer**
- A terminal, Command Prompt, PowerShell, or VS Code terminal
- **No additional libraries to install.** The project uses only Python's standard library (`math`).

## Project Files

```text
smart-grocery-store/
├── smart_grocery_store.py   # Main application
└── README.md                # Project documentation
```

## How to Run

1. Download `smart_grocery_store.py` and `README.md`.
2. Save both files in the same folder.
3. Open that folder in VS Code or open a terminal there.
4. Run:

   ```bash
   python smart_grocery_store.py
   ```

   On Windows, if `python` is not recognized, try:

   ```powershell
   py smart_grocery_store.py
   ```

5. Type a menu number (`1` through `8`) and press Enter.

## Application Menu

```text
====================================
SMART GROCERY STORE SYSTEM
====================================
1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit
Enter your choice (1-8):
```

## Example Usage

### 1. Add Products

Choose option `1` and enter the product details. For example:

```text
Enter product ID: 101
Enter product name: Milk
Enter category: Dairy
Enter product price: 250
Enter available stock: 20
Product 'Milk' added successfully.
```

Add another product with ID `102`, name `Bread`, category `Bakery`, price `120`, and stock `3`.

### 2. Process a Sale

Choose option `5`:

```text
Enter product ID: 101
Product: Milk | Available stock: 20
Enter purchase quantity: 2

--- Purchase Summary ---
Product ID:       101
Product Name:     Milk
Quantity Sold:    2
Unit Price:       Rs. 250.00
Total Amount:     Rs. 500.00
Remaining Stock:  18
Sale completed successfully.
```

A sale is **cancelled** if the product ID does not exist, the product is out of stock, or the quantity exceeds stock. Cancelled sales do not change stock or sales records.

### 3. Generate a Store Report

Choose option `7` after adding the two example products and selling two units of Milk:

```text
========== STORE REPORT ==========
Total number of products:   2
Total available stock:      21
Total sales transactions:   1
Total revenue generated:    Rs. 500.00

Products with stock below 5 units:
  - Bread (ID: 102, Stock: 3)

Highest-priced product: Milk (Rs. 250.00)
Lowest-priced product:  Bread (Rs. 120.00)
==================================
```

## Data Structures

The application primarily uses **two lists of dictionaries**, both starting empty:

```python
products = []
sales_records = []
```

A product is stored like this:

```python
{
    "id": 101,
    "name": "Milk",
    "category": "Dairy",
    "price": 250.0,
    "stock": 20
}
```

After a successful sale, a sales record looks like this:

```python
{
    "product_id": 101,
    "product_name": "Milk",
    "quantity_sold": 2,
    "total_amount": 500.0
}
```

## Important Functions

| Function | Purpose |
|---|---|
| `main()` | Runs the menu loop and selects actions. |
| `add_new_product()` | Validates details, checks unique IDs, and appends the product. |
| `view_all_products()` | Prints inventory in tabular form. |
| `search_product()` | Finds products by ID or partial name. |
| `update_product_stock()` | Adds to stock or sets a replacement quantity. |
| `process_customer_sale()` | Verifies stock, calculates totals, updates inventory, and appends a sale record. |
| `view_sales_records()` | Displays completed sales. |
| `generate_store_report()` | Calculates and displays store-wide statistics. |
| `find_product_by_id()` | Looks up a product dictionary by its numeric ID. |

Additional helper functions validate positive integers, non-negative integers, non-empty text, and prices.

## Input Validation

- **Product IDs:** positive whole numbers only; duplicate IDs are rejected.
- **Product names and categories:** cannot be blank.
- **Prices:** must be positive, finite numbers; stored to two decimal places.
- **Initial and replacement stock:** non-negative whole numbers (including zero).
- **Stock additions and purchase quantities:** positive whole numbers.
- **Sales:** never allowed to exceed available stock.
- **Invalid menu choices:** display an error instead of crashing.

## Testing Checklist

Try these cases manually:

- [ ] Add a product successfully.
- [ ] Try to add another product with the same ID.
- [ ] Enter an invalid price, empty name, or negative stock.
- [ ] Search using an existing ID and a partial, mixed-case name.
- [ ] Search for a product that does not exist.
- [ ] Add more stock and replace stock with zero.
- [ ] Try to sell more units than are available.
- [ ] Complete a valid sale; check reduced stock and the sales record.
- [ ] Generate a report with products and sales, and with no products.
- [ ] Exit the application with option `8`.

## Limitations

- **Data is kept in memory only.** All products and sales records reset when the program exits or restarts.
- The program is **terminal-based**, not a graphical desktop or web application.
- Each successful purchase is recorded as a separate transaction for **one product at a time**.
- Revenue is the sum of completed sales; costs, profit, taxes, and discounts are not tracked.

These are outside the requested assignment scope. A future version could save data using JSON, CSV, or SQLite.

## Learning Outcomes

Completing this project demonstrates how to:

1. Store related data with Python dictionaries inside lists.
2. Organize a program into reusable functions.
3. Handle interactive menus using loops and conditional statements.
4. Validate input before modifying inventory and sales records.
5. Use calculations and loops to generate a business report.

---

**Project:** Smart Grocery Store Management System  
**Language:** Python  
**Application type:** Command-line / terminal
