import os
import sys
import json

FILE_PATH = "player_data.json"

def load_all_games() -> dict:
    """Load all saved games from the file, or return an empty dictionary if none exist."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_game(player: dict) -> None:
    """Save only the current player's progress without overwriting all data."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r+") as file:
            try:
                all_games = json.load(file)
            except json.JSONDecodeError:
                all_games = {}
    else:
        all_games = {}

    all_games[player["name"].lower()] = player  # Update only this player's data

    with open(FILE_PATH, "w") as file:
        json.dump(all_games, file, indent=4)

def load_game() -> dict:
    """Load game for a specific player based on their name."""
    name = input("Enter your name: ").strip()
    all_games = load_all_games()
    player_name = name.lower()
    
    if player_name in all_games:
        saved_game = all_games[player_name]

        if saved_game.get("lives", 0) <= 0:
            print("No lives remain. Starting a new game.")
            return start_new_game(name)

        choice = input(f"Resume saved game (Level {saved_game.get('level')})? (yes/no): ").strip().lower()
        if choice.startswith("y"):
            return saved_game
        else:
            return start_new_game(name)
    
    print("No saved game found. Starting a new one.")
    return start_new_game(name)

def start_new_game(name: str) -> dict:
    """Initialize a new game for the player."""
    player_data = {"name": name, "lives": 3, "level": 1}
    save_game(player_data)  # Save only the new player's data
    return player_data

def handle_exit(player: dict) -> None:
    """Handles game exit with saving progress."""
    save_game(player)
    print("Game saved. Exiting...")
    sys.exit(0)
