import time
from utils.helpers import ask_riddle, solve_puzzle
from model.player import get_player_level, update_player_level

def enchanted_forest(player):
    print("\n" + "-"*60)
    time.sleep(2)
    print("Stepping through a dense curtain of ancient trees, you enter the Enchanted Forest.")
    time.sleep(3)
    print()
    print("The air is heavy with magic and the whispers of long-forgotten secrets echo around you.")
    time.sleep(2)
    print()
    print("A mysterious voice echoes from the depths of the woods...")
    time.sleep(2)
    
    # Riddle challenge.
    riddle_prompt = ("Riddle: I speak without a mouth and hear without ears. "
                     "I have no body, but I come alive with the wind. What am I?")
    if not ask_riddle(riddle_prompt, "echo", player):
        return
    
    print()
    time.sleep(2)
    print("Impressed by your answer, an ancient tree reveals a carved sequence on its trunk.")
    time.sleep(3)
    
    # Puzzle challenge.
    puzzle_prompt = ("Puzzle: The tree displays the following sequence of numbers:\n"
                     "2, 4, 8, 16, ?\n"
                     "What is the next number in the sequence?")
    if not solve_puzzle(puzzle_prompt, "32", player):
        return
    
    print()
    time.sleep(2)
    print("The forest path now splits into two routes:")
    print("1. Follow the narrow trail into the shadowed woods (leads to Shadow Realm)")
    print("2. Take the sunlit clearing leading to an ancient tower (leads to Celestial Tower)")
    
    choice = input("> ").strip()
    if choice == "1":
        update_player_level(player, 4)
        from views.shadow_realm import shadow_realm
        shadow_realm(player)
    elif choice == "2":
        update_player_level(player, 5)
        from views.celestial_tower import celestial_tower
        celestial_tower(player)
    else:
        print("Invalid choice. Returning to main area.")
