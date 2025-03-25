def create_player(name: str, lives: int, level: int) -> dict[str, str | int]:
    """Creates a player dictionary with name, lives, and level."""
    return {"name": name, "lives": lives, "level": level}

def get_player_name(player: dict[str, str | int]) -> str:
    """Returns the player's name."""
    return str(player["name"])

def get_player_lives(player: dict[str, str | int]) -> int:
    """Returns the player's remaining lives."""
    return int(player["lives"])

def get_player_level(player: dict[str, str | int]) -> int:
    """Returns the player's current level."""
    return int(player["level"])

def update_player_lives(player: dict[str, str | int], lives: int) -> None:
    """Updates the player's lives."""
    player["lives"] = lives

def update_player_level(player: dict[str, str | int], level: int) -> None:
    """Updates the player's level."""
    player["level"] = level
