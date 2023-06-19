class Character:
    def __init__(self, character_dict) -> None:
        self.name = character_dict["name"]

        self.friends = character_dict["friends"]

        self.interests = character_dict["interests"]

        self.disinterests = character_dict["disinterests"]

        print(self.name, self.friends, self.interests, self.disinterests)
