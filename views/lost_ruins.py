import time
from utils.helpers import ask_riddle, solve_puzzle
from model.player import get_player_level, update_player_level

def lost_ruins(player):
    print("\n" + "-"*60)
    time.sleep(2)
    print("Stepping into the Lost Ruins, you are surrounded by crumbling arches and faded murals.")
    time.sleep(3)
    print()
    print("A mural depicting ancient priests praying to forgotten gods fills you with a sense of solemn mystery.")
    time.sleep(2)
    print()
    
    # Riddle challenge.
    riddle_prompt = "Riddle: The more you take, the more you leave behind. What am I?"
    if not ask_riddle(riddle_prompt, "footsteps", player):
        return
    
    print()
    time.sleep(2)
    print("As you examine the mural, a hidden plaque slides open, revealing a sequence of letters.")
    time.sleep(3)
    
    # Puzzle challenge.
    puzzle_prompt = ("Puzzle: The plaque shows the sequence: A, C, F, J, ?\n"
                     "Based on the pattern, what letter comes next?")
    if not solve_puzzle(puzzle_prompt, "o", player):
        return
    
    print()
    time.sleep(2)
    print("A secret passage opens. Two paths now lie ahead:")
    print("1. Descend into a fiery undercroft (leads to Molten Core)")
    print("2. Climb the crumbling castle stairs (leads to Abandoned Castle)")
    
    choice = input("> ").strip()
    if choice == "1":
        update_player_level(player, 6)
        from views.molten_core import molten_core
        molten_core(player)
    elif choice == "2":
        update_player_level(player, 7)
        from views.abandoned_castle import abandoned_castle
        abandoned_castle(player)
    else:
        print("Invalid choice. Returning to main area.")
