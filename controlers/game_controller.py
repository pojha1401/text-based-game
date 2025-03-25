#time module to have sleep time
import time

# internal moduless
from views.lost_ruins import lost_ruins
from views.molten_core import molten_core
from views.shadow_realm import shadow_realm
from views.celestial_tower import celestial_tower
from views.enchanted_forest import enchanted_forest
from services.save_load import load_game, save_game
from views.abandoned_castle import abandoned_castle
from model.player import (
    create_player,
    get_player_name,
    get_player_lives,
    get_player_level,
    update_player_lives,
    update_player_level,
)

def start_game():
    """Initialize or load game state and start the appropriate scenario."""
    player = load_game()
    if not player:
        name = input("Enter your name: ")
        player = create_player(name=name, lives=3, level=1)

    print(f"\nWelcome, {get_player_name(player)}!")
    print(f"You have {get_player_lives(player)} lives remaining.\n")
    time.sleep(2)

    start_scenario(player)  # Start the game from the player's current level

def start_scenario(player):
    """Dynamically call the correct scenario based on the player's level."""
    scenarios = {
        1: start_decision,        # Initial choice between forest and ruins
        2: enchanted_forest,      # Leads to Shadow Realm or Celestial Tower
        3: lost_ruins,            # Leads to Molten Core or Abandoned Castle
        4: shadow_realm,          # Leads to Final Stage
        5: celestial_tower,       # Leads to Final Stage
        6: molten_core,           # Leads to Final Stage
        7: abandoned_castle,      # Leads to Final Stage
    }

    scenario = scenarios.get(get_player_level(player))
    if scenario:
        scenario(player)
    else:
        print(f" {get_player_name(player)}, you've reached the Final Stage! To be continued...")

def start_decision(player):
    """Initial decision: Choose between Enchanted Forest and Lost Ruins."""
    while True:
        print("\nYou stand at a crossroad:")
        print("1 Enchanted Forest")
        print("2 Lost Ruins")
        choice = input("> ").strip()

        if choice == "1":
            update_player_level(player, 2)
            enchanted_forest(player)
            break
        elif choice == "2":
            update_player_level(player, 3)
            lost_ruins(player)
            break
        else:
            print("Invalid choice! Please select 1 or 2.")

    save_game(player)
