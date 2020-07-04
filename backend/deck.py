import os
import json


class Deck:

    def __init__(self, name="Deck", mainboard=None, sideboard=None, maybeboard=None):
        # Avoid mutable default values
        if mainboard is None:
            mainboard = list()
        if sideboard is None:
            sideboard = list()
        if maybeboard is None:
            maybeboard = list()
        # Define class-wise variables
        self.__deck_name = None
        self.__mainboard = None
        self.__sideboard = None
        self.__maybeboard = None
        # Store the values of the board
        self.set_mainboard(mainboard)
        self.set_sideboard(sideboard)
        self.set_maybeboard(maybeboard)

    def get_name(self) -> str:
        return self.__deck_name

    def set_name(self, name: str):
        self.__deck_name = name

    # Returns a copy of the mainboard. This is to prevent accidental modification of the board
    def get_mainboard(self) -> list:
        return [item for item in self.__mainboard]

    # Stores a copy of the board. This is to prevent accidental modification of the board
    def set_mainboard(self, board: list):
        # TODO: Ensure that the board being passes in only contains valid cards
        self.__mainboard = [item for item in board]

    # Returns a copy of the sideboard. This is to prevent accidental modification of the board
    def get_sideboard(self) -> list:
        return [item for item in self.__sideboard]

    # Stores a copy of the board. This is to prevent accidental modification of the board
    def set_sideboard(self, board: list):
        # TODO: Ensure that the board being passes in only contains valid cards
        self.__sideboard = [item for item in board]

    # Returns a copy of the maybeboard. This is to prevent accidental modification of the board
    def get_maybeboard(self) -> list:
        return [item for item in self.__maybeboard]

    # Stores a copy of the board. This is to prevent accidental modification of the board
    def set_maybeboard(self, board: list):
        # TODO: Ensure that the board being passes in only contains valid cards
        self.__maybeboard = [item for item in board]


# Accepts a pack to a deck json file as input
# Returns a deck object, or None if the path does not point to a usable file
def load_deck(path: str):
    if not os.path.isfile(path):
        return None
    # In case loading the deck fails when opening the file
    try:
        with open(path, "r", encoding="utf8") as deck_file:
            file_contents = json.load(deck_file)
        # Extact the fields from the JSON
        deck_name = file_contents["name"]
        deck_mainboard = file_contents["mainboard"]
        deck_sideboard = file_contents["sideboard"]
        deck_maybeboard = file_contents["maybeboard"]
        # Create the deck object
        deck = Deck(
            name=deck_name,
            mainboard=deck_mainboard,
            sideboard=deck_sideboard,
            maybeboard=deck_maybeboard
        )
        # Return the deck
        return deck
    except IOError:
        print("Error loading file:", path)
        return None


# Attempt to save a deck file to the specified folder
# Returns true if, and only if, saving was successful
def save_deck(folder_path: str, deck: Deck) -> bool:
    if not os.path.isdir(folder_path):
        return False
    # Build the file path. We use os.pathsep here to help with system independence
    file_path = "".join((folder_path, os.pathsep, deck.get_name()))
    try:
        deck_dict = {
            "name": deck.get_name(),
            "mainboard": deck.get_mainboard(),
            "sideboard": deck.get_sideboard(),
            "maybeboard": deck.get_maybeboard()
        }
        with open(file_path, "r", encoding="UTF8") as outfile:
            json.dump(deck_dict, file_path)
        return True
    except IOError as error:
        print("Unexpected error when saving deck:", error)
        return False
    return True
