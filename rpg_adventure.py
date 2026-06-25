"""
Program: RPG Adventure Simulator
Author: Jaylen Johnson
Purpose: A text-based RPG game where the player explores areas, battles monsters, earns gold, and manages inventory.
Starter code: No starter code was used.
Date: 6/28/2026
"""

print("Welcome to RPG Adventure Simulator!")
print("Create your hero and begin your journey.")

player_name = input("\nEnter your hero's name: ")
player = {
    "name": player_name,
    "level": 1,
    "health": 30,
    "max_health": 30,
    "attack": 6,
    "gold": 10
}
inventory = ["Health Potion", "Rusty Sword"]
print(f"\nWelcome, {player['name']}!")

while True:
    print("\n==========================")
    print(" RPG Adventure Simulator")
    print("==========================")
    print("1. View Character")
    print("2. Explore")
    print("3. View Inventory")
    print("4. Rest")
    print("5. Visit Shop")
    print("6. Quit")

    choice = input("\nChoose an option (1-6): ")

    if choice == "1":
        print("\nCharacter Stats")
        print("---------------")
        print(f"Name: {player['name']}")
        print(f"Level: {player['level']}")
        print(f"Health: {player['health']}/{player['max_health']}")
        print(f"Attack: {player['attack']}")
        print(f"Gold: {player['gold']}")
        input("\nPress Enter to continue...")

    elif choice == "3":
        print("\nInventory")
        print("---------")

        for item in inventory:
            print(f"- {item}")

        input("\nPress Enter to continue...")

    elif choice == "6":
        print("\nThanks for playing. Goodbye!")
        break