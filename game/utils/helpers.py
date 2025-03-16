import sys
import time
from services.save_load import handle_exit
from model.player import get_player_lives, update_player_lives

def ask_question(prompt: str, correct_answer: str, player: dict) -> bool:
    """function for riddles and puzzles."""
    while True:
        print("\n" + prompt)
        user_input = input("> ").strip().lower()

        if user_input in ["exit", "pause"]:
            confirm = input("Do you really want to exit the game? (yes/no) ").strip().lower()
            if confirm == "yes":
                handle_exit(player)
            continue

        if user_input == correct_answer.lower():
            print("Correct!")
            time.sleep(2)
            return True
        else:
            print("Incorrect! You lose a life.")
            update_player_lives(player, get_player_lives(player) - 1)

            if get_player_lives(player) <= 0:
                print("You have no lives left!")
                sys.exit(0)

            time.sleep(2)
            print("Please try again.\n")
