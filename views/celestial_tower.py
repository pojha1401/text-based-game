import time
from utils.helpers import ask_riddle, solve_puzzle
from model.player import get_player_level, update_player_level

def celestial_tower(player):
    print("\n" + "-"*60)
    time.sleep(2)
    print("You approach the Celestial Tower, its stone walls etched with cosmic symbols and constellations.")
    time.sleep(3)
    print()
    print("A wise sage stands at the entrance, his eyes reflecting the light of distant stars.")
    time.sleep(2)
    print()
    
    # Riddle challenge.
    riddle_prompt = "Riddle: I wax and wane, guiding the night with my glow. What am I?"
    if not ask_riddle(riddle_prompt, "moon", player):
        return
    
    print()
    time.sleep(2)
    print("The sage unfurls a star chart that displays a mysterious numerical pattern.")
    time.sleep(3)
    
    # Puzzle challenge.
    puzzle_prompt = (
    "Puzzle: The star chart shows the following grid:\n"
    "A B C\n"
    "D E F\n"
    "G H I\n"
    "Rotate the grid 90 degrees clockwise and enter the new arrangement (e.g., G D A H E B I F C):"
    )
    if not solve_puzzle(puzzle_prompt, "G D A H E B I F C", player):
        return
    
    print()
    time.sleep(2)
    update_player_level(player, 7)   
    print("The sage nods in approval and leads you to the Final Stage.")
    time.sleep(2)
    from views.final_stage import final_stage
    final_stage(player)
