import time
from utils.helpers import ask_riddle, solve_puzzle
from model.player import get_player_level, update_player_level

def molten_core(player):
    print("\n" + "-"*60)
    time.sleep(2)
    print("You descend into the Molten Core, where the heat is nearly unbearable and rivers of lava flow.")
    time.sleep(3)
    print()
    print("A towering fiery sentinel appears, its eyes burning with intensity.")
    time.sleep(2)
    print()
    
    # Riddle challenge.
    riddle_prompt = ("Riddle: I am always hungry, I must always be fed; the finger I lick will soon turn red. What am I?")
    if not ask_riddle(riddle_prompt, "fire", player):
        return
    
    print()
    time.sleep(2)
    print("The sentinel reveals an ancient inscription carved into basalt, showing a number series.")
    time.sleep(3)
    
    # Puzzle challenge.
    puzzle_prompt = ("Puzzle: The inscription reads: 5, 9, 15, 23, ?\n"
                     "What is the next number in the series?")
    if not solve_puzzle(puzzle_prompt, "33", player):
        return
    
    print()
    time.sleep(2)
    update_player_level(player, 8)
    print("The fiery sentinel steps aside, revealing the path to the Final Stage.")
    time.sleep(2)
    from views.final_stage import final_stage
    final_stage(player)
