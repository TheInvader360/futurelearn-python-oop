class Room():

    def __init__(self, room_name):
        """Initialise room with a name and no description, linked rooms, character, or item"""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def describe(self):
        """Prints out description"""
        print("The " + self.name)
        print("--------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("'" + direction + "': " + room.get_name())

    def link_room(self, room_to_link, direction):
        """Adds a room to this room's linked rooms dictionary"""
        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        """Returns the room found in the specified direction (if exists)"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self

    def set_name(self, room_name):
        """Setter (name)"""
        self.name = room_name

    def get_name(self):
        """Getter (name)"""
        return self.name

    def set_description(self, room_description):
        """Setter (description)"""
        self.description = room_description

    def get_description(self):
        """Getter (description)"""
        return self.description

    def set_character(self, character):
        """Setter (character)"""
        self.character = character

    def get_character(self):
        """Getter (character)"""
        return self.character

    def set_item(self, item):
        """Setter (item)"""
        self.item = item

    def get_item(self):
        """Getter (item)"""
        return self.item

