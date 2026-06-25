"""
Program: RPG Adventure Simulator
Author: Jaylen Johnson
Purpose: A text-based RPG game where the player explores areas, battles monsters, earns gold, and manages inventory.
Starter code: No starter code was used.
Date: 6/28/2026
"""

import random

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

locations = ("Forest", "Cave", "Abandoned Road")

monsters = [
    {"name": "Goblin", "health": 10, "attack": 3, "gold": 5},
    {"name": "Skeleton", "health": 15, "attack": 4, "gold": 8},
    {"name": "Orc", "health": 20, "attack": 5, "gold": 12}
]

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

    elif choice == "2":
        location = random.choice(locations)
        event = random.choice(["gold", "item", "monster", "nothing"])

        print(f"\nYou explore the {location}.")

        if event == "gold":
            found_gold = random.randint(3, 10)
            player["gold"] += found_gold
            print(f"You found {found_gold} gold!")

        elif event == "item":
            found_item = random.choice(["Old Shield", "Magic Herb", "Iron Dagger"])
            inventory.append(found_item)
            print(f"You found a {found_item}!")

        elif event == "monster":
            monster = random.choice(monsters)

            print(f"\nA wild {monster['name']} appears!")

            monster_health = monster["health"]

            while monster_health > 0 and player["health"] > 0:
                print(f"\nYour Health: {player['health']}")
                print(f"{monster['name']} Health: {monster_health}")

                input("Press Enter to attack...")

                monster_health -= player["attack"]
                print(f"You hit the {monster['name']}!")

                if monster_health <= 0:
                    break

                player["health"] -= monster["attack"]
                print(f"The {monster['name']} attacks you!")

            if player["health"] > 0:
                print(f"\nYou defeated the {monster['name']}!")
                player["gold"] += monster["gold"]
                print(f"You earned {monster['gold']} gold!")

            else:
                print("\nYou were defeated...")
                player["health"] = player["max_health"]
                print("You wake up safely back at camp.")

        elif event == "nothing":
            print("You did not find anything this time.")

        input("\nPress Enter to continue...")

    elif choice == "3":
        print("\nInventory")
        print("---------")

        for item in inventory:
            print(f"- {item}")

        input("\nPress Enter to continue...")

    elif choice == "4":
        player["health"] = player["max_health"]
        print("\nYou rest at camp and recover your health.")
        print(f"Health restored to {player['health']}/{player['max_health']}.")
        input("\nPress Enter to continue...")

    elif choice == "6":
        print("\nThanks for playing. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")
        input("\nPress Enter to continue...")
