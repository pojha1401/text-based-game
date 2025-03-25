import time
from utils.helpers import ask_riddle, solve_puzzle
from model.player import get_player_level, update_player_level

from views.final_stage import final_stage

def shadow_realm(player):
    print("\n" + "-"*60)
    time.sleep(2)
    print("You step into the Shadow Realm, where dim light barely penetrates the oppressive darkness.")
    time.sleep(3)
    print()
    print("A spectral figure emerges from the gloom and speaks in a cold, ancient tone.")
    time.sleep(2)
    print()
    
    # Riddle challenge.
    riddle_prompt = ("Riddle: I have cities but no houses, forests but no trees, and rivers but no water. What am I?")
    if not ask_riddle(riddle_prompt, "map", player):
        return
    
    print()
    time.sleep(2)
    print("The figure leads the way to a shadowy portal.")
    time.sleep(3)
    print("Carved into the frame of the portal is an encoded message, its letters glowing faintly:")
    time.sleep(2)
    print("\n'Khoor Zruog'\n")
    time.sleep(2)
    print("Beside the portal lies the spectral remains of a previous adventurer.")
    time.sleep(3)
    print("Clutched in the skeleton's hand is a faded note. You pick it up and read:")
    time.sleep(2)
    print("\n'To those who follow: Beware the shifting shadows. The portal's cipher first word is Hello.'\n")
    time.sleep(3)
    print("The note continues: 'To unlock the portal, reverse the shift and speak the true message.'\n")
    time.sleep(2)
    
    # Puzzle challenge.
    puzzle_prompt = (
    "Puzzle: The portal's encoded message reads: 'Khoor Zruog'\n"
    "Enter the decoded message:"
    )
    if not solve_puzzle(puzzle_prompt, "Hello World", player):
        return
        
    print()
    time.sleep(2)
    update_player_level(player, 6)
    print("Satisfied, the spectral figure leads you onward to the Final Stage.")
    time.sleep(2)
    final_stage(player)
