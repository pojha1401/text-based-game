import time
from utils.helpers import ask_riddle, solve_puzzle
from model.player import get_player_level, update_player_level

def abandoned_castle(player):
    print("\n" + "-" * 60)
    time.sleep(2)
    print("You enter the Abandoned Castle, where silence and decay reign over the grand hall.")
    time.sleep(3)
    print()
    print("An ancient portrait of a noble family hangs askew, its eyes seeming to follow your every move.")
    time.sleep(2)
    print()
    
    # Puzzle challenge.
    puzzle_prompt = (
        "Puzzle: The mosaic shows a sequence of colored tiles: Red, Blue, Green, Yellow, Red.\n"
        "Each color represents a direction:\n"
        "Red = North, Blue = East, Green = South, Yellow = West.\n"
        "Enter the sequence of directions (e.g., North, East, South, West, North):"
    )
    if not solve_puzzle(puzzle_prompt, "North, East, South, West, North", player):
        return
    
    print()
    time.sleep(2)
    print("Beneath the portrait, a mosaic on the stone floor reveals a complex pattern.")
    time.sleep(3)
    
    # Puzzle challenge.
    puzzle_prompt = (
        "Puzzle: Analyze the mosaic below and count the total number of squares (include both small squares and larger ones formed by grouping):\n"
        "  +---+---+---+\n"
        "  |   |   |   |\n"
        "  +---+---+---+\n"
        "  |   |   |   |\n"
        "  +---+---+---+\n"
        "  |   |   |   |\n"
        "  +---+---+---+\n"
        "Enter the total number of squares:"
    )
    if not solve_puzzle(puzzle_prompt, "14", player):
        return
    
    print()
    time.sleep(2)
    
    # Update player level using function-based approach
    update_player_level(player, 9)
    
    print("A secret door opens in the wall, and you step through to the Final Stage.")
    time.sleep(2)
    
    from views.final_stage import final_stage
    final_stage(player)
