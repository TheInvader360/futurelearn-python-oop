from room import Room
from character import Character, Enemy, Friend
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")
ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "s")
dining_hall.link_room(kitchen, "n")
dining_hall.link_room(ballroom, "w")
ballroom.link_room(dining_hall, "e")

vlad = Enemy("Vlad", "A scary vampire")
vlad.set_conversation("I'm always looking for my necks victim!")
vlad.set_weakness("stake")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... Rgrhl... Braaaaains!")
dave.set_weakness("bat")

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Konnichiwa!")

kitchen.set_character(vlad)
dining_hall.set_character(dave)
ballroom.set_character(catrina)

bat = Item("bat", "A solid looking cricket bat")
stake = Item("stake", "A wooden stake, sharpened at one end")

ballroom.set_item(bat)
dining_hall.set_item(stake)

current_room = kitchen
inventory = []
game_over = False

while game_over == False:
    print("\n")
    current_room.describe()

    current_room_character = current_room.get_character()
    if current_room_character is not None:
        current_room_character.describe()

    current_room_item = current_room.get_item()
    if current_room_item is not None:
        current_room_item.describe()

    command = input("> ")

    if command in ["n", "s", "e", "w"]: #north/south/east/west
        current_room = current_room.move(command)
    elif command == "t": #talk
        if current_room_character == None:
            print("There's nobody here to talk to!")
        else:
            current_room_character.talk()
    elif command == "f": #fight
        if current_room_character == None or isinstance(current_room_character, Friend):
            print("There's nobody here to fight!")
        else:
            print("Choose your weapon...")
            weapon = input()
            if weapon in inventory:
                if current_room_character.fight(weapon) == True:
                    print("A winner is you!")
                    current_room.set_character(None)
                    if Enemy.defeated_total == 2:
                        print("Congratulations, you defeated all the enemies!")
                        game_over = True
                else:
                    print("Game over, man. Game over!")
                    game_over = True
            else:
                print("You haven't got a '" + weapon + "' in your inventory!")
    elif command == "h": #hug
        if current_room_character == None:
            print("There's nobody here to hug!")
        else:
            if isinstance(current_room_character, Enemy):
                print("Danger, Will Robinson!")
            else:
                current_room_character.hug()
    elif command == "g": #get
        if current_room_item == None:
            print("There's no gettable item in this room!")
        else:
            print("You got the " + current_room_item.get_name())
            inventory.append(current_room_item.get_name())
            current_room.set_item(None)
    elif command == "i": #inventory
        if len(inventory) == 0:
            print("Your inventory is empty!")
        else:
            print("Your inventory:")
            for item in inventory:
                print(item)
    else:
        print("¯\_(ツ)_/¯")
