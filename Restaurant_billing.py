import pandas as pd
import numpy as np

menu = {
    "Item": ["IDLY", "PLAIN DOSA", "POORI", "CHAPPATHI", "PAROTTA" , "VADA", "VEN PONGAL" , "SWEET PONGAL", "MASALA DOSA" , "RAVA DOSA", "GHEE ROAST"],
    "Price": [10,40,35,30,45,12,25,35,50,75,85]
}
menu_df = pd.DataFrame(menu)
def display_menu():
    print("Menu:")
    print(menu_df)

def take_order():
    order = []
    while True:
        item = input("Enter the item name (or 'done' to finish ordering): ")
        if item.lower() == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        order.append({"Item": item, "Quantity": quantity})
    return order
def calculate_bill(order):
    bill = 0
    bill_items = []
    for item in order:
        item_name = item["Item"]
        quantity = item["Quantity"]
        item_price = menu_df.loc[menu_df["Item"] == item_name, "Price"].values[0]
        total_price = item_price * quantity
        bill += total_price
        bill_items.append({"Item": item_name, "Quantity": quantity, "Price": total_price})
    return bill, bill_items
def display_bill(bill, bill_items):
    print("\nBill:")
    bill_df = pd.DataFrame(bill_items)
    print(bill_df)
    print(f"Total: ${bill:.2f}")
def main():
    print("Welcome to the Restaurant!")
    while True:
        print("\nOptions:")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_menu()
        elif choice == '2':
            order = take_order()
            bill, bill_items = calculate_bill(order)
            display_bill(bill, bill_items)
        elif choice == '3':
            print("Thank you for using the Restaurant Billing System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()