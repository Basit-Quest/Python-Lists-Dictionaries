"""Smart Grocery Store Management System.

Run with: python smart_grocery_store.py
Data is stored in memory and resets when the program closes.
"""

import math


# Lists of dictionaries are the main data structures of the application.
products = []
sales_records = []


def get_positive_integer(prompt):
    """Keep asking until the user enters a whole number greater than zero."""
    while True:
        value = input(prompt).strip()
        if value.isdecimal() and int(value) > 0:
            return int(value)
        print("Invalid input. Please enter a positive whole number.")


def get_non_negative_integer(prompt):
    """Accept zero or a positive whole number (but not a negative number)."""
    while True:
        value = input(prompt).strip()
        if value.isdecimal():
            return int(value)
        print("Invalid input. Please enter a whole number of 0 or more.")


def get_valid_text(prompt):
    """Reject empty product names and categories."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_valid_price():
    """Validate that the price is a finite number greater than zero."""
    while True:
        value = input("Enter product price: ").strip()
        try:
            price = float(value)
            if math.isfinite(price) and round(price, 2) > 0:
                return round(price, 2)
        except ValueError:
            pass
        print("Invalid price. Enter a number greater than zero.")


def find_product_by_id(product_id):
    """Return the matching product dictionary, or None if not found."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def show_product_details(product):
    """Display every field in one product dictionary."""
    print("\n--- Product Details ---")
    print(f"Product ID:      {product['id']}")
    print(f"Product Name:    {product['name']}")
    print(f"Category:        {product['category']}")
    print(f"Price:           Rs. {product['price']:.2f}")
    print(f"Available Stock: {product['stock']}")


def add_new_product():
    print("\n--- Add New Product ---")
    while True:
        product_id = get_positive_integer("Enter product ID: ")
        if find_product_by_id(product_id) is None:
            break
        print("This product ID already exists. Please use a unique ID.")

    name = get_valid_text("Enter product name: ")
    category = get_valid_text("Enter category: ")
    price = get_valid_price()
    stock = get_non_negative_integer("Enter available stock: ")

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock,
    }
    products.append(product)  # Add a new product dictionary to the list.
    print(f"Product '{name}' added successfully.")


def view_all_products():
    print("\n--- All Products ---")
    if not products:
        print("No products have been added yet.")
        return

    print(f"{'ID':<8} {'Name':<22} {'Category':<18} {'Price (Rs.)':>13} {'Stock':>8}")
    print("-" * 75)
    for product in products:
        print(
            f"{product['id']:<8} "
            f"{product['name'][:22]:<22} "
            f"{product['category'][:18]:<18} "
            f"{product['price']:>13.2f} "
            f"{product['stock']:>8}"
        )


def search_product():
    print("\n--- Search Product ---")
    print("1. Search by Product ID")
    print("2. Search by Product Name")
    choice = input("Choose search option (1 or 2): ").strip()

    if choice == "1":
        product_id = get_positive_integer("Enter product ID: ")
        product = find_product_by_id(product_id)
        if product is None:
            print("Product not found.")
        else:
            show_product_details(product)
    elif choice == "2":
        search_text = get_valid_text("Enter product name: ").casefold()
        found = False
        for product in products:
            # Partial, case-insensitive matching (e.g., 'mil' finds 'Milk').
            if search_text in product["name"].casefold():
                show_product_details(product)
                found = True
        if not found:
            print("Product not found.")
    else:
        print("Invalid search option. Please choose 1 or 2.")


def update_product_stock():
    print("\n--- Update Product Stock ---")
    product_id = get_positive_integer("Enter product ID: ")
    product = find_product_by_id(product_id)
    if product is None:
        print("Product not found.")
        return

    print(f"Current stock for {product['name']}: {product['stock']}")
    print("1. Add more stock")
    print("2. Set stock to a new quantity")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        additional_stock = get_positive_integer("Enter quantity to add: ")
        product["stock"] += additional_stock
    elif choice == "2":
        product["stock"] = get_non_negative_integer("Enter new stock quantity: ")
    else:
        print("Invalid option. Stock was not changed.")
        return

    print(f"Stock updated. {product['name']} now has {product['stock']} unit(s).")


def process_customer_sale():
    print("\n--- Process Customer Sale ---")
    product_id = get_positive_integer("Enter product ID: ")
    product = find_product_by_id(product_id)
    if product is None:
        print("Sale cancelled: product not found.")
        return

    print(f"Product: {product['name']} | Available stock: {product['stock']}")
    if product["stock"] == 0:
        print("Sale cancelled: this product is out of stock.")
        return

    quantity = get_positive_integer("Enter purchase quantity: ")
    if quantity > product["stock"]:
        print("Sale cancelled: insufficient stock available.")
        return

    total_amount = round(quantity * product["price"], 2)
    product["stock"] -= quantity  # Reduce stock only after validation.

    sale = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity_sold": quantity,
        "total_amount": total_amount,
    }
    sales_records.append(sale)  # Record only successful sales.

    print("\n--- Purchase Summary ---")
    print(f"Product ID:       {product['id']}")
    print(f"Product Name:     {product['name']}")
    print(f"Quantity Sold:    {quantity}")
    print(f"Unit Price:       Rs. {product['price']:.2f}")
    print(f"Total Amount:     Rs. {total_amount:.2f}")
    print(f"Remaining Stock:  {product['stock']}")
    print("Sale completed successfully.")


def view_sales_records():
    print("\n--- Sales Records ---")
    if not sales_records:
        print("No sales have been recorded yet.")
        return

    print(f"{'No.':<6} {'ID':<8} {'Product Name':<24} {'Quantity':>10} {'Total (Rs.)':>15}")
    print("-" * 70)
    for index, sale in enumerate(sales_records, start=1):
        print(
            f"{index:<6} {sale['product_id']:<8} "
            f"{sale['product_name'][:24]:<24} "
            f"{sale['quantity_sold']:>10} {sale['total_amount']:>15.2f}"
        )


def generate_store_report():
    print("\n========== STORE REPORT ==========")
    total_stock = 0
    low_stock_products = []

    for product in products:
        total_stock += product["stock"]
        if product["stock"] < 5:
            low_stock_products.append(product)

    total_revenue = 0
    for sale in sales_records:
        total_revenue += sale["total_amount"]

    print(f"Total number of products:   {len(products)}")
    print(f"Total available stock:      {total_stock}")
    print(f"Total sales transactions:   {len(sales_records)}")
    print(f"Total revenue generated:    Rs. {total_revenue:.2f}")

    print("\nProducts with stock below 5 units:")
    if low_stock_products:
        for product in low_stock_products:
            print(f"  - {product['name']} (ID: {product['id']}, Stock: {product['stock']})")
    else:
        print("  None")

    if products:
        highest_price_product = max(products, key=lambda product: product["price"])
        lowest_price_product = min(products, key=lambda product: product["price"])
        print(
            f"\nHighest-priced product: {highest_price_product['name']} "
            f"(Rs. {highest_price_product['price']:.2f})"
        )
        print(
            f"Lowest-priced product:  {lowest_price_product['name']} "
            f"(Rs. {lowest_price_product['price']:.2f})"
        )
    else:
        print("\nHighest-priced product: None (no products)")
        print("Lowest-priced product:  None (no products)")

    print("==================================")


def display_menu():
    print("\n====================================")
    print("SMART GROCERY STORE SYSTEM")
    print("====================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")


def main():
    # Continue displaying the menu until the user selects Exit.
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_new_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product_stock()
        elif choice == "5":
            process_customer_sale()
        elif choice == "6":
            view_sales_records()
        elif choice == "7":
            generate_store_report()
        elif choice == "8":
            print("Thank you for using the Smart Grocery Store System. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")
