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

# --- Car Data ---
# In a real application, this data might come from a database or a CSV file.
CAR_MODELS = [
    {
        "id": 1, "make": "Toyota", "model": "Camry", "type": "Sedan", "year": 2023,
        "price": 25000, "fuel_economy_mpg": 32,
        "features": ["Bluetooth", "Backup Camera", "Cruise Control", "Lane Assist"]
    },
    {
        "id": 2, "make": "Honda", "model": "CR-V", "type": "SUV", "year": 2023,
        "price": 28000, "fuel_economy_mpg": 29,
        "features": ["Bluetooth", "Backup Camera", "All-Wheel Drive", "Sunroof"]
    },
    {
        "id": 3, "make": "Ford", "model": "F-150", "type": "Truck", "year": 2023,
        "price": 35000, "fuel_economy_mpg": 20,
        "features": ["Bluetooth", "Towing Package", "Backup Camera", "4x4"]
    },
    {
        "id": 4, "make": "Tesla", "model": "Model 3", "type": "Electric", "year": 2023,
        "price": 42000, "fuel_economy_mpg": 130, # MPGe for electric
        "features": ["Autopilot", "Large Touchscreen", "Premium Sound", "Glass Roof"]
    },
    {
        "id": 5, "make": "BMW", "model": "3 Series", "type": "Sedan", "year": 2023,
        "price": 45000, "fuel_economy_mpg": 28,
        "features": ["Leather Seats", "Navigation", "Harman Kardon Sound", "Sport Package"]
    },
    {
        "id": 6, "make": "Hyundai", "model": "Elantra", "type": "Sedan", "year": 2024,
        "price": 22000, "fuel_economy_mpg": 35,
        "features": ["Bluetooth", "Backup Camera", "Apple CarPlay", "Android Auto"]
    },
    {
        "id": 7, "make": "Kia", "model": "Sportage", "type": "SUV", "year": 2024,
        "price": 27000, "fuel_economy_mpg": 28,
        "features": ["Bluetooth", "Backup Camera", "Panoramic Sunroof", "Wireless Charging"]
    },
    {
        "id": 8, "make": "Subaru", "model": "Outback", "type": "Wagon", "year": 2023,
        "price": 30000, "fuel_economy_mpg": 29,
        "features": ["All-Wheel Drive", "Eyesight Driver Assist", "Roof Rails", "Heated Seats"]
    },
    {
        "id": 9, "make": "Chevrolet", "model": "Bolt EV", "type": "Electric", "year": 2023,
        "price": 26500, "fuel_economy_mpg": 120, # MPGe
        "features": ["One-Pedal Driving", "Large Touchscreen", "DC Fast Charging"]
    },
    {
        "id": 10, "make": "Mazda", "model": "CX-5", "type": "SUV", "year": 2023,
        "price": 29000, "fuel_economy_mpg": 27,
        "features": ["Bluetooth", "Backup Camera", "Premium Interior", "G-Vectoring Control"]
    }
]

AVAILABLE_CAR_TYPES = sorted(list(set(car["type"] for car in CAR_MODELS)))
ALL_FEATURES = sorted(list(set(feature for car in CAR_MODELS for feature in car["features"])))


# --- Recommendation Logic ---

def get_user_preferences():
    """Gets car preferences from the user."""
    preferences = {}
    print("Let's find your perfect car! Please answer a few questions.\n")

    # Budget
    while True:
        try:
            preferences['max_price'] = float(input("What is your maximum budget (e.g., 30000)? $"))
            if preferences['max_price'] > 0:
                break
            else:
                print("Budget must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numerical value for budget.")

    # Car Type
    print("\nAvailable car types:")
    for i, car_type in enumerate(AVAILABLE_CAR_TYPES, 1):
        print(f"{i}. {car_type}")
    print(f"{len(AVAILABLE_CAR_TYPES) + 1}. Any / No Preference")

    while True:
        try:
            type_choice = int(input(f"Choose a car type (1-{len(AVAILABLE_CAR_TYPES) + 1}): "))
            if 1 <= type_choice <= len(AVAILABLE_CAR_TYPES):
                preferences['type'] = AVAILABLE_CAR_TYPES[type_choice - 1]
                break
            elif type_choice == len(AVAILABLE_CAR_TYPES) + 1:
                preferences['type'] = None # No preference
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(AVAILABLE_CAR_TYPES) + 1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Features
    print("\nWhat features are important to you? (Optional)")
    print("Available features:")
    for i, feature in enumerate(ALL_FEATURES, 1):
        print(f"  {i}. {feature}")
    print("Enter feature numbers separated by commas (e.g., 1, 3, 5), or press Enter to skip.")

    selected_features = []
    while True:
        feature_input = input("Your choices: ").strip()
        if not feature_input:
            break # Skip if empty
        try:
            chosen_indices = [int(x.strip()) for x in feature_input.split(',')]
            valid_choices = True
            temp_features = []
            for index in chosen_indices:
                if 1 <= index <= len(ALL_FEATURES):
                    temp_features.append(ALL_FEATURES[index - 1])
                else:
                    print(f"Invalid feature number: {index}. Please choose from the list.")
                    valid_choices = False
                    break
            if valid_choices:
                selected_features = list(set(temp_features)) # Remove duplicates
                break
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
    preferences['features'] = selected_features
    print("-" * 30)
    return preferences

def recommend_cars(preferences, car_models):
    """Recommends cars based on user preferences."""
    recommended = []
    for car in car_models:
        # Price check
        if car['price'] > preferences['max_price']:
            continue

        # Type check
        if preferences['type'] and car['type'].lower() != preferences['type'].lower():
            continue

        # Feature check (all selected features must be present in the car)
        if preferences['features']:
            missing_feature = False
            for required_feature in preferences['features']:
                if required_feature not in car['features']:
                    missing_feature = True
                    break
            if missing_feature:
                continue

        recommended.append(car)
    return recommended

def display_recommendations(cars):
    """Displays the recommended cars."""
    if not cars:
        print("Sorry, no cars match your criteria with the current models.")
        print("You might want to adjust your preferences or check back later for new models.")
        return

    display_header("RECOMMENDED CARS")
    for car in cars:
        print(f"Make: {car['make']}, Model: {car['model']} ({car['year']})")
        print(f"  Type: {car['type']}")
        print(f"  Price: ${car['price']:,}")
        fuel_label = "MPGe" if car['type'].lower() == "electric" else "MPG"
        print(f"  Fuel Economy: {car['fuel_economy_mpg']} {fuel_label}")
        print(f"  Features: {', '.join(car['features'])}")
        print("-" * 30)

# --- Main Application Logic ---
def main():
    """Main function to run the car recommendation system."""
    while True:
        clear_screen()
        display_header("Car Recommendation System")
        print("Welcome! Let's find the best car for you.")
        print("\n1. Get Car Recommendations")
        print("2. View All Available Cars")
        print("3. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            clear_screen()
            user_prefs = get_user_preferences()
            clear_screen()
            print("\n--- Your Preferences ---")
            print(f"Max Budget: ${user_prefs['max_price']:,}")
            print(f"Car Type: {user_prefs['type'] if user_prefs['type'] else 'Any'}")
            print(f"Desired Features: {', '.join(user_prefs['features']) if user_prefs['features'] else 'None'}")
            print("-" * 30)
            recommendations = recommend_cars(user_prefs, CAR_MODELS)
            display_recommendations(recommendations)
            input("\nPress Enter to return to the main menu...")
        elif choice == '2':
            clear_screen()
            display_header("ALL AVAILABLE CAR MODELS")
            if not CAR_MODELS:
                print("No car models are currently available.")
            else:
                for car in CAR_MODELS:
                    print(f"{car['make']} {car['model']} ({car['year']}) - ${car['price']:,} ({car['type']})")
                    print(f"  Features: {', '.join(car['features'])}")
                    print("-" * 20)
            input("\nPress Enter to return to the main menu...")
        elif choice == '3':
            print("Thank you for using the Car Recommendation System. Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    main()
