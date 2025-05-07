import csv
import os

# --- Configuration ---
MENU_CSV_FILE = 'restaurant_menu.csv'

# --- Helper Functions ---

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title):
    """Prints a formatted header."""
    print("=" * 40)
    print(f"{title:^40}")
    print("=" * 40)
    print()

def load_menu():
    """Loads the menu from the CSV file."""
    menu = {}
    if not os.path.exists(MENU_CSV_FILE):
        # Create a dummy CSV if it doesn't exist
        print(f"'{MENU_CSV_FILE}' not found. Creating a sample menu.")
        sample_menu_data = [
            {'id': '1', 'name': 'Margherita Pizza', 'category': 'Main Course', 'price': 12.99},
            {'id': '2', 'name': 'Caesar Salad', 'category': 'Appetizer', 'price': 8.50},
            {'id': '3', 'name': 'Spaghetti Carbonara', 'category': 'Main Course', 'price': 15.00},
            {'id': '4', 'name': 'Chocolate Lava Cake', 'category': 'Dessert', 'price': 7.25},
            {'id': '5', 'name': 'Iced Tea', 'category': 'Beverage', 'price': 2.50},
            {'id': '6', 'name': 'Bruschetta', 'category': 'Appetizer', 'price': 6.00},
            {'id': '7', 'name': 'Grilled Salmon', 'category': 'Main Course', 'price': 18.75},
            {'id': '8', 'name': 'Tiramisu', 'category': 'Dessert', 'price': 7.00},
            {'id': '9', 'name': 'Cappuccino', 'category': 'Beverage', 'price': 3.50},
        ]
        try:
            with open(MENU_CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ['id', 'name', 'category', 'price']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(sample_menu_data)
        except IOError:
            print(f"Error: Could not create or write to '{MENU_CSV_FILE}'. Please check permissions.")
            return {} # Return empty menu if creation fails

    try:
        with open(MENU_CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            item_id_counter = 1
            for row in reader:
                try:
                    # Use 'id' from CSV if present, otherwise generate one
                    item_id = row.get('id', str(item_id_counter))
                    menu[item_id] = {
                        'name': row['name'],
                        'category': row['category'],
                        'price': float(row['price'])
                    }
                    item_id_counter +=1
                except KeyError:
                    print(f"Warning: Skipping row due to missing 'name', 'category', or 'price': {row}")
                except ValueError:
                    print(f"Warning: Skipping row due to invalid price for item '{row.get('name', 'Unknown')}': {row}")
        if not menu:
            print(f"Warning: No items loaded from '{MENU_CSV_FILE}'. The file might be empty or incorrectly formatted after the header.")
    except FileNotFoundError:
        print(f"Error: The menu file '{MENU_CSV_FILE}' was not found.")
        return {} # Return empty menu
    except Exception as e:
        print(f"An unexpected error occurred while loading the menu: {e}")
        return {} # Return empty menu
    return menu

def display_menu(menu):
    """Displays the restaurant menu, categorized."""
    if not menu:
        print("The menu is currently empty or could not be loaded.")
        return

    display_header("MENU")
    categories = {}
    for item_id, details in menu.items():
        if details['category'] not in categories:
            categories[details['category']] = []
        categories[details['category']].append((item_id, details))

    for category, items in categories.items():
        print(f"--- {category} ---")
        for item_id, details in items:
            print(f"  {item_id}. {details['name']:<25} ${details['price']:.2f}")
        print()
    print("-" * 40)

def take_order(menu):
    """Allows the user to take an order."""
    if not menu:
        print("Cannot take orders as the menu is unavailable.")
        return {}

    order = {}
    display_menu(menu)
    print("Enter item ID to add to order. Type 'done' when finished.")

    while True:
        choice = input("Enter item ID (or 'done'): ").strip().lower()
        if choice == 'done':
            break

        if choice in menu:
            item_name = menu[choice]['name']
            while True:
                try:
                    quantity = int(input(f"Enter quantity for {item_name}: "))
                    if quantity > 0:
                        break
                    else:
                        print("Quantity must be a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a number for quantity.")

            if choice in order:
                order[choice]['quantity'] += quantity
            else:
                order[choice] = {
                    'name': menu[choice]['name'],
                    'price': menu[choice]['price'],
                    'quantity': quantity
                }
            print(f"{quantity} x {item_name} added to your order.")
        else:
            print("Invalid item ID. Please choose from the menu.")
        print()

    return order

def display_order(order):
    """Displays the current order details."""
    if not order:
        print("Your order is currently empty.")
        return 0.0 # Return 0 total if order is empty

    display_header("CURRENT ORDER")
    total_bill = 0
    for item_id, details in order.items():
        subtotal = details['price'] * details['quantity']
        print(f"- {details['name']} (x{details['quantity']}) : ${subtotal:.2f}")
        total_bill += subtotal
    print("-" * 40)
    print(f"TOTAL: ${total_bill:.2f}")
    print("-" * 40)
    return total_bill

def calculate_bill(order):
    """Calculates and displays the final bill."""
    if not order:
        print("No order to calculate bill for.")
        return

    total_bill = display_order(order) # display_order now returns the total
    # In a real system, you might add taxes, service charges, etc.
    print("\nThank you for your order!")
    return total_bill


# --- Main Application Logic ---
def main():
    """Main function to run the restaurant management system."""
    current_order = {}
    menu_items = load_menu()

    if not menu_items:
        print("Failed to load menu. Exiting application.")
        # Attempt to create a dummy menu file if loading failed and it doesn't exist
        if not os.path.exists(MENU_CSV_FILE):
            print(f"Please ensure '{MENU_CSV_FILE}' exists and is correctly formatted, or run the script again to generate a sample.")
        return

    while True:
        clear_screen()
        display_header("Restaurant Management System")
        print("1. View Menu")
        print("2. Place/Modify Order")
        print("3. View Current Order")
        print("4. Checkout & Get Bill")
        print("5. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            clear_screen()
            display_menu(menu_items)
            input("\nPress Enter to return to the main menu...")
        elif choice == '2':
            clear_screen()
            current_order = take_order(menu_items) # take_order now returns the full order
            clear_screen()
            display_order(current_order)
            input("\nPress Enter to return to the main menu...")
        elif choice == '3':
            clear_screen()
            display_order(current_order)
            input("\nPress Enter to return to the main menu...")
        elif choice == '4':
            clear_screen()
            if not current_order:
                print("Your order is empty. Please add items before checking out.")
            else:
                calculate_bill(current_order)
                current_order = {} # Reset order after checkout
            input("\nPress Enter to return to the main menu...")
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    # Create a dummy CSV file if it doesn't exist for the first run
    if not os.path.exists(MENU_CSV_FILE):
        print(f"Menu file '{MENU_CSV_FILE}' not found. A sample file will be created on first run if needed.")
        # The load_menu function will handle creation if it's missing.
    main()
