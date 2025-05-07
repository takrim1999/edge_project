import os

# --- Helper Functions ---
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title):
    """Prints a formatted header."""
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)
    print()

# --- Hotel Data ---
# In a real application, this data might come from a database or a CSV file.
HOTEL_ROOMS = [
    {
        "id": 101, "type": "Single", "price_per_night": 75.00,
        "amenities": ["Wi-Fi", "TV", "Air Conditioning"], "is_available": True
    },
    {
        "id": 102, "type": "Single", "price_per_night": 80.00,
        "amenities": ["Wi-Fi", "TV", "Air Conditioning", "Mini-fridge"], "is_available": False # Booked
    },
    {
        "id": 201, "type": "Double", "price_per_night": 120.00,
        "amenities": ["Wi-Fi", "TV", "Air Conditioning", "Coffee Maker"], "is_available": True
    },
    {
        "id": 202, "type": "Double", "price_per_night": 130.00,
        "amenities": ["Wi-Fi", "TV", "Air Conditioning", "Coffee Maker", "Balcony"], "is_available": True
    },
    {
        "id": 301, "type": "Suite", "price_per_night": 250.00,
        "amenities": ["Wi-Fi", "Large TV", "Air Conditioning", "Jacuzzi", "Living Area", "Mini-bar"], "is_available": True
    },
    {
        "id": 302, "type": "Suite", "price_per_night": 275.00,
        "amenities": ["Wi-Fi", "Large TV", "Air Conditioning", "Jacuzzi", "Living Area", "Mini-bar", "Ocean View"], "is_available": False # Booked
    },
    {
        "id": 401, "type": "Family", "price_per_night": 180.00,
        "amenities": ["Wi-Fi", "TV", "Air Conditioning", "Bunk Beds", "Kitchenette"], "is_available": True
    },
    {
        "id": 103, "type": "Single", "price_per_night": 70.00,
        "amenities": ["Wi-Fi", "TV"], "is_available": True # Basic single
    }
]

AVAILABLE_ROOM_TYPES = sorted(list(set(room["type"] for room in HOTEL_ROOMS)))
ALL_AMENITIES = sorted(list(set(amenity for room in HOTEL_ROOMS for amenity in room["amenities"])))

# --- Recommendation & Management Logic ---

def get_booking_preferences():
    """Gets room booking preferences from the user."""
    preferences = {}
    print("Let's find the perfect room for your stay!\n")

    # Budget per night
    while True:
        try:
            preferences['max_price_per_night'] = float(input("What is your maximum budget per night (e.g., 150)? $"))
            if preferences['max_price_per_night'] > 0:
                break
            else:
                print("Budget must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    # Room Type
    print("\nAvailable room types:")
    for i, room_type in enumerate(AVAILABLE_ROOM_TYPES, 1):
        print(f"{i}. {room_type}")
    print(f"{len(AVAILABLE_ROOM_TYPES) + 1}. Any / No Preference")

    while True:
        try:
            type_choice = int(input(f"Choose a room type (1-{len(AVAILABLE_ROOM_TYPES) + 1}): "))
            if 1 <= type_choice <= len(AVAILABLE_ROOM_TYPES):
                preferences['type'] = AVAILABLE_ROOM_TYPES[type_choice - 1]
                break
            elif type_choice == len(AVAILABLE_ROOM_TYPES) + 1:
                preferences['type'] = None # No preference
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(AVAILABLE_ROOM_TYPES) + 1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Amenities
    print("\nWhat amenities are important for your stay? (Optional)")
    print("Available amenities:")
    for i, amenity in enumerate(ALL_AMENITIES, 1):
        print(f"  {i}. {amenity}")
    print("Enter amenity numbers separated by commas (e.g., 1, 3), or press Enter to skip.")

    selected_amenities = []
    while True:
        amenity_input = input("Your choices: ").strip()
        if not amenity_input:
            break # Skip if empty
        try:
            chosen_indices = [int(x.strip()) for x in amenity_input.split(',')]
            valid_choices = True
            temp_amenities = []
            for index in chosen_indices:
                if 1 <= index <= len(ALL_AMENITIES):
                    temp_amenities.append(ALL_AMENITIES[index - 1])
                else:
                    print(f"Invalid amenity number: {index}. Please choose from the list.")
                    valid_choices = False
                    break
            if valid_choices:
                selected_amenities = list(set(temp_amenities)) # Remove duplicates
                break
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
    preferences['amenities'] = selected_amenities
    print("-" * 30)
    return preferences

def recommend_rooms(preferences, rooms):
    """Recommends available rooms based on user preferences."""
    recommended = []
    for room in rooms:
        if not room['is_available']:
            continue

        # Price check
        if room['price_per_night'] > preferences['max_price_per_night']:
            continue

        # Type check
        if preferences['type'] and room['type'].lower() != preferences['type'].lower():
            continue

        # Amenity check (all selected amenities must be present in the room)
        if preferences['amenities']:
            missing_amenity = False
            for required_amenity in preferences['amenities']:
                if required_amenity not in room['amenities']:
                    missing_amenity = True
                    break
            if missing_amenity:
                continue

        recommended.append(room)
    return recommended

def display_rooms(rooms_list, title="AVAILABLE ROOMS"):
    """Displays a list of rooms."""
    if not rooms_list:
        print("No rooms match the criteria or are currently available.")
        return

    display_header(title)
    for room in rooms_list:
        availability = "Available" if room['is_available'] else "Booked"
        print(f"Room ID: {room['id']}, Type: {room['type']}")
        print(f"  Price per night: ${room['price_per_night']:.2f}")
        print(f"  Amenities: {', '.join(room['amenities'])}")
        print(f"  Status: {availability}")
        print("-" * 30)

def book_room(room_id, rooms_data):
    """Marks a room as booked."""
    for room in rooms_data:
        if room['id'] == room_id:
            if room['is_available']:
                room['is_available'] = False
                print(f"Room {room_id} has been successfully booked.")
                return True
            else:
                print(f"Sorry, Room {room_id} is already booked.")
                return False
    print(f"Error: Room ID {room_id} not found.")
    return False

def checkout_room(room_id, rooms_data):
    """Marks a room as available."""
    for room in rooms_data:
        if room['id'] == room_id:
            if not room['is_available']:
                room['is_available'] = True
                print(f"Room {room_id} has been successfully checked out and is now available.")
                return True
            else:
                print(f"Error: Room {room_id} is already available.")
                return False
    print(f"Error: Room ID {room_id} not found.")
    return False


# --- Main Application Logic ---
def main():
    """Main function to run the hotel management system."""
    # HOTEL_ROOMS is our 'database' for this example
    global HOTEL_ROOMS

    while True:
        clear_screen()
        display_header("Hotel Management System")
        print("Welcome! How can we assist you today?")
        print("\n1. Find & Recommend Rooms")
        print("2. View All Rooms")
        print("3. Book a Room")
        print("4. Check-out from Room")
        print("5. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            clear_screen()
            user_prefs = get_booking_preferences()
            clear_screen()
            print("\n--- Your Preferences ---")
            print(f"Max Budget per Night: ${user_prefs['max_price_per_night']:.2f}")
            print(f"Room Type: {user_prefs['type'] if user_prefs['type'] else 'Any'}")
            print(f"Desired Amenities: {', '.join(user_prefs['amenities']) if user_prefs['amenities'] else 'None'}")
            print("-" * 30)
            recommendations = recommend_rooms(user_prefs, HOTEL_ROOMS)
            display_rooms(recommendations, "RECOMMENDED ROOMS FOR YOU")
            input("\nPress Enter to return to the main menu...")
        elif choice == '2':
            clear_screen()
            display_rooms(HOTEL_ROOMS, "ALL HOTEL ROOMS")
            input("\nPress Enter to return to the main menu...")
        elif choice == '3': # Book a Room
            clear_screen()
            display_rooms([room for room in HOTEL_ROOMS if room['is_available']], "AVAILABLE ROOMS FOR BOOKING")
            if not any(room['is_available'] for room in HOTEL_ROOMS):
                print("Sorry, no rooms are currently available for booking.")
            else:
                try:
                    room_id_to_book = int(input("Enter the ID of the room you want to book: "))
                    book_room(room_id_to_book, HOTEL_ROOMS)
                except ValueError:
                    print("Invalid Room ID format. Please enter a number.")
            input("\nPress Enter to return to the main menu...")
        elif choice == '4': # Check-out from Room
            clear_screen()
            display_rooms([room for room in HOTEL_ROOMS if not room['is_available']], "CURRENTLY BOOKED ROOMS")
            if not any(not room['is_available'] for room in HOTEL_ROOMS):
                print("No rooms are currently booked.")
            else:
                try:
                    room_id_to_checkout = int(input("Enter the ID of the room to check-out: "))
                    checkout_room(room_id_to_checkout, HOTEL_ROOMS)
                except ValueError:
                    print("Invalid Room ID format. Please enter a number.")
            input("\nPress Enter to return to the main menu...")
        elif choice == '5':
            print("Thank you for using the Hotel Management System. Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    main()
