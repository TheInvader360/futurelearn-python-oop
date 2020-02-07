from room import Room
from character import Character, Enemy, Friend

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

current_room = kitchen
dead = False

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    if command in ["n", "s", "e", "w"]:
        current_room = current_room.move(command)
    elif command == "t":
        if inhabitant == None:
            print("There's nobody here to talk to!")
        else:
            inhabitant.talk()
    elif command == "f":
        if inhabitant == None or isinstance(inhabitant, Friend):
            print("There's nobody here to fight!")
        else:
            print("Choose your weapon...")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("A winner is you!")
                current_room.set_character(None)
            else:
                print("Game over, man. Game over!")
                dead = True
    elif command == "h":
        if inhabitant == None:
            print("There's nobody here to hug!")
        else:
            if isinstance(inhabitant, Enemy):
                print("Danger, Will Robinson!")
            else:
                inhabitant.hug()
    else:
        print("¯\_(ツ)_/¯")
