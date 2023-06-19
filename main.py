import os
import json

from character import Character

VERSION = "0.1.1"

HOBBIES = [
    "Video Games",
    "Music",
    "Fine Food",
    "Reading",
    "Movies",
    "Art",
    "Hiking",
    "Photography",
    "Board Games",
    "Cooking",
    "Exercise",
    "Travel",
    "Socializing",
]


class EmptyValues(Exception):
    pass


def identify_friends() -> list:
    friends = []
    friends.append(input("Enter a close friend's first name: ").capitalize())
    friends.append(input("Enter another close friend's first name: ").capitalize())
    friends.append(input("Enter another close friend's first name (Last one!): ").capitalize())
    return friends


def identify_interests() -> list:
    print("\nNow we will define your interests! Press ENTER to continue.")
    interests = []
    i = 1
    while i < 4:
        hobby_item_no = 1
        for item in HOBBIES:
            print(f"{hobby_item_no}: {item}")
            hobby_item_no += 1
        try:
            hobby = int(input("Enter NUMBER of most interesting hobby on list: ")[:2])
        except:
            print("Invalid number. Enter a numer. Please try again...\n")
            continue
        try:
            interests.append(HOBBIES.pop(hobby - 1))
        except:
            print("Invalid selection. Number is off the list. Please try again...\n")
            continue
        i += 1

    return interests


def identify_disinterests():
    input("\nNow we will establish your disinterests... Press ENTER to continue.")
    disinterests = []
    i = 1
    while i < 3:
        hobby_item_no = 1
        for item in HOBBIES:
            print(f"{hobby_item_no}: {item}")
            hobby_item_no += 1
        try:
            hobby = int(input("Enter NUMBER of LEAST interesting hobby on list: ")[:2])
        except:
            print("Invalid number. Enter a numer. Please try again...\n")
            continue
        try:
            disinterests.append(HOBBIES.pop(hobby - 1))
        except:
            print("Invalid selection. Number is off the list. Please try again...\n")
            continue
        i += 1

    return disinterests


def create_character() -> dict:
    print("Creating new character...")

    character_data = {}

    character_data["name"] = input(
        "Enter character first name. This will overwrite other saves with this name: "
    ).capitalize()

    character_data["friends"] = identify_friends()

    character_data[f"interests"] = identify_interests()

    character_data[f"disinterests"] = identify_disinterests()

    return character_data


if __name__ == "__main__":
    print(f"Version {VERSION}")

    saved_characters = [x.split(".")[0] for x in os.listdir("saved_chars")]
    if len(saved_characters):
        character = input(
            f"Saved characters found: {saved_characters}. Enter character name to continue or press ENTER to skip load: "
        )
        character = True
    else:
        character = False

    if character:
        try:
            with open(f"saved_chars/{character}.json") as f:
                character_data = json.load(f)
                print(character_data)
            if any(x == "" for x in character_data.values()):
                raise EmptyValues
        except EmptyValues as e:
            print("Empty entries found in character save file. Must remake character to use.")
            os.remove(f"saved_chars/{character}.json")
            character = False
        except Exception as e:
            print(e)
            print("Could not load character. Creating new character.")
            character = False

    while not character:
        character_data = create_character()

        confirmation = input(
            f"Here's the character you created: {character_data}. Type SAVE to save, or REDO to remake: "
        )

        if confirmation == "SAVE":
            print("Saving character")
            json_object = json.dumps(character_data, indent=4)

            with open(f"saved_chars/{character_data['name']}.json", "w") as outfile:
                outfile.write(json_object)

            character = True
        elif confirmation == "REDO":
            continue
        else:
            continue

    character = Character(character_data)
