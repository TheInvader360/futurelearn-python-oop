class Character():

    def __init__(self, char_name, char_description):
        """Initialise character with a name and description"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Prints out description"""
        print("'" + self.name + "' is here!" + " (" + self.description + ")")

    def talk(self):
        """Prints out conversation (if set)"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """Prints out message to notify that you can't fight character"""
        print(self.name + " doesn't want to fight with you")
        return True

    def set_conversation(self, conversation):
        """Setter (conversation)"""
        self.conversation = conversation


class Enemy(Character):

    defeated_total = 0

    def __init__(self, char_name, char_description):
        """Initialise enemy with a name and description and no weakness"""
        super().__init__(char_name, char_description)
        self.weakness = None

    def fight(self, combat_item):
        """Fight is won if combat_item matches enemy weakness (return true), else fight is lost (return false)"""
        if combat_item == self.weakness:
            print("You smite " + self.name + " with the " + combat_item)
            Enemy.defeated_total += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer!")
            return False

    def set_weakness(self, weakness):
        """Setter (weakness)"""
        self.weakness = weakness

    def get_weakness(self):
        """Getter (weakness)"""
        return self.weakness


class Friend(Character):

    def __init__(self, char_name, char_description):
        """Initialise friend with a name and description"""
        super().__init__(char_name, char_description)

    def hug(self):
        """Prints out message to notify that friend hugs you back"""
        print(self.name + " hugs you back!")

