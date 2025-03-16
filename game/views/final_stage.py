import time
from utils.helpers import ask_riddle, solve_puzzle
from model.player import get_player_level, update_player_level

def final_stage(player):
    print("\n" + "-"*60)
    time.sleep(2)
    print("You have reached the Final Stage, a vast chamber where destiny awaits.")
    time.sleep(3)
    print()
    print("Before you stands an ancient door guarded by an ethereal presence.")
    time.sleep(2)
    print()
    
    # Riddle challenge.
    riddle_prompt = ("Riddle: I bind the past and the future; I am always ahead but never seen. What am I?")
    if not ask_riddle(riddle_prompt, "time", player):
        return
    
    print()
    time.sleep(2)
    print("The door reveals an inscription with a series of numbers etched by long-forgotten hands.")
    time.sleep(3)
    
    # Puzzle challenge.
    puzzle_prompt = ("Puzzle: The sequence reads: 1, 3, 6, 10, ?\n"
                     "What is the next number in this series?")
    if not solve_puzzle(puzzle_prompt, "15", player):
        return
    
    print()
    time.sleep(2)
    update_player_level(player, 10)
    print("The ancient door glows warmly as it slowly opens, revealing the treasure of wisdom.")
    time.sleep(3)
    print("CONGRATULATIONS! You have successfully completed your adventure.")
