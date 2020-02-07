class Item():

    def __init__(self, item_name, item_description):
        """Initialise item with a name and description"""
        self.name = item_name
        self.description = item_description

    def describe(self):
        """Prints out description"""
        print("There is a '" + self.name + "' here!" + " (" + self.description + ")")

    def get_name(self):
        """Getter (name)"""
        return self.name

    def set_name(self, item_name):
        """Setter (name)"""
        self.name = item_name

    def get_description(self):
        """Getter (description)"""
        return self.description

    def set_description(self, item_description):
        """Setter (description)"""
        self.description = item_description

