"""
Program: RPG Adventure Simulator
Author: Jaylen Johnson
Purpose: A text-based RPG game where the player explores areas, battles monsters, earns gold, and manages inventory.
Starter code: No starter code was used.
Date: 6/28/2026
"""

import random

def view_character(player):
    """Display the player's current character statistics."""
    print("\nCharacter Stats")
    print("---------------")
    print(f"Name: {player['name']}")
    print(f"Level: {player['level']}")
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Attack: {player['attack']}")
    print(f"Gold: {player['gold']}")
    input("\nPress Enter to continue...")

def view_inventory(inventory):
    """Display all items currently in the player's inventory."""
    print("\nInventory")
    print("---------")

    for item in inventory:
        print(f"- {item}")

    input("\nPress Enter to continue...")

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

boss_defeated = False

shop_items = {
    "Health Potion": 8,
    "Iron Sword": 20,
    "Steel Shield": 15
}

while True:
    print("\n==========================")
    print(" RPG Adventure Simulator")
    print("==========================")
    print("1. View Character")
    print("2. Explore")
    print("3. View Inventory")
    print("4. Use Health Potion")
    print("5. Rest")
    print("6. Visit Shop")
    print("7. Challenge Dragon King")
    print("8. Quit")

    choice = input("\nChoose an option (1-8): ")

    if choice == "1":
        view_character(player)

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
                player["level"] += 1
                player["attack"] += 1
                player["max_health"] += 2
                player["health"] = player["max_health"]

                print(f"You earned {monster['gold']} gold!")
                print("You leveled up!")
                print(f"Level: {player['level']}")
                print(f"Attack increased to {player['attack']}.")
                print(f"Max health increased to {player['max_health']}.")

            else:
                print("\nYou were defeated...")
                player["health"] = player["max_health"]
                print("You wake up safely back at camp.")

        elif event == "nothing":
            print("You did not find anything this time.")

        input("\nPress Enter to continue...")

    elif choice == "3":
        view_inventory(inventory)

    elif choice == "4":
        if "Health Potion" in inventory:
            inventory.remove("Health Potion")

            heal_amount = 15
            player["health"] += heal_amount

            if player["health"] > player["max_health"]:
                player["health"] = player["max_health"]

            print("\nYou drink a Health Potion.")
            print(f"You recovered {heal_amount} health.")
            print(f"Current Health: {player['health']}/{player['max_health']}")
        else:
            print("\nYou don't have a Health Potion!")

        input("\nPress Enter to continue...")

    elif choice == "5":
        player["health"] = player["max_health"]
        print("\nYou rest at camp and recover your health.")
        print(f"Health restored to {player['health']}/{player['max_health']}.")
        input("\nPress Enter to continue...")

    elif choice == "6":
        print("\nShop")
        print("----")
        print(f"Your Gold: {player['gold']}")

        for item, price in shop_items.items():
            print(f"{item}: {price} gold")

        item_choice = input("\nEnter the item name to buy or type 'exit': ")

        if item_choice == "exit":
            print("\nYou leave the shop.")

        elif item_choice in shop_items:
            item_price = shop_items[item_choice]

            if player["gold"] >= item_price:
                player["gold"] -= item_price
                inventory.append(item_choice)
                print(f"\nYou bought {item_choice}!")

                if item_choice == "Iron Sword":
                    player["attack"] += 3
                    print("Your attack increased by 3.")

                elif item_choice == "Steel Shield":
                    player["max_health"] += 5
                    player["health"] += 5
                    print("Your max health increased by 5.")

            else:
                print("\nYou do not have enough gold.")

        else:
            print("\nThat item is not sold here.")

        input("\nPress Enter to continue...")

    elif choice == "7":
        if player["level"] >= 3:
            print("\nYou challenge the Dragon King...")
            print("After a difficult battle, you defeat the Dragon King!")
            print("You win the game!")
            boss_defeated = True
            break
        else:
            print("\nYou are not strong enough yet.")
            print("Reach level 3 before challenging the Dragon King.")
            input("\nPress Enter to continue...")

    elif choice == "8":
        print("\nThanks for playing. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 8.")
        input("\nPress Enter to continue...")
