# Author:   Ivan Perez
# Program:  TextBasedGame.py
# Date:     12/10/21

# The dictionary links a room to other rooms. All objects, except for 'Vestibule' contain an item key and value
rooms = {
    'Vestibule': {'East': 'Main Hall', 'item': ''},
    'Main Hall': {'North': 'Gallery', 'East': 'Saloon', 'West': 'Vestibule', 'item': '500g strawberries'},
    'Saloon': {'West': 'Main Hall', 'South': 'Den', 'item': '175g castor sugar'},
    'Den': {'North': 'Saloon', 'item': 'Icing sugar'},
    'Gallery': {'North': 'Banquet Room', 'West': 'Billiard Room', 'East': 'Library', 'South': 'Main Hall', 'item': '500g jam sugar'},
    'Billiard Room': {'East': 'Gallery', 'item': '300ml double cream'},
    'Library': {'West': 'Gallery', 'North': 'Music Room', 'item': '175g unsalted butter'},
    'Music Room': {'South': 'Library', 'item': '175g self-raising flour'},
    'Banquet Room': {'West': 'Kitchen', 'East': 'Formal Dining Room', 'item': '3 large eggs'},
    'Formal Dining Room': {'West': 'Banquet Room', 'item': '1tsp vanilla extract'},
    'Kitchen': {'East': 'Banquet Room', 'item': 'boss'}
}

# def instructions function prints out game title and command instructions.
# returns nothing.


def instructions():
    print("The Great British Bakeoff Text Game")
    print("Collect 8 items to make a perfect bake and win the game, or fail")
    print("and disappoint Paul Hollywood and Prue Leith.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: grab 'item name'")

# def greeting function prints out game intro/story.
# returns nothing.


def greeting():
    print("While in your kitchen, you shuffle through the pantry looking for snacks.")
    print("You are trying to hurry because the latest episode of The Great British Bake Off is about to start. While reaching for a bag of chips on the top shelf, you hit your head and everything goes dark...\n")
    print("You awaken inside of a great and elegantly decorated victorian era entrance. Before you stand two familiar figures, one tall and lanky, and the other, short and stout.")
    print("You quickly recognizes the individuals as Noel Fielding and Matt Lucas, the two presenters for The Great British Bake Off.")
    print("'Is this a dream?' you think to yourself as you look around, seeing that you're alone with these two.")

    print("\nNoel states 'Welcome contestant! Your challenge today has been set by Paul Hollywood.")
    print("You are to bake 12 Mini Victoria Sponge Cakes.")
    print("But there's a twist! You won't find the ingredients in the kitchen.")
    print("You'll have to explore the many rooms of The Welford Estate to find each ingredient needed.'")

    print("\nWith this, Noel hands you a single sheet of paper. Looking over it, you see it's a list of ingredients and instructions,\n")

    ingredientsJam = [
        '500g (1lb 2oz) strawberries, hulled and halved', '500g (1lb 2oz) jam sugar']
    ingredientsSponge = ['175g (6 oz) unsalted butter, at room temperature, plus extra for greasing', '175g (6 oz) caster sugar', '3 large free-range eggs, beaten',
                         '1 tsp vanilla extract', '175g (6 oz) self-raising flour', '300ml (10½ fl oz) double cream', 'icing sugar, for dusting']
    # print both lists for all ingredients
    print("For the jam:")
    for num in ingredientsJam:
        print(num)

    print("\nFor the sponge:")
    for num in ingredientsSponge:
        print(num)

    print("\nLooking back up to the duo, Matt says 'Once you've gathered your ingredients, make your way to the kitchen where Paul and Prue await to judge your bake.' The duo, in unison, state 'Ready, set, Bake!\n")


# def endGameText takes in boolean value. if True, prints winning statement. if False, prints losing statement

def endGameText(bool):
    if bool == True:
        print("You stand before Paul and Prue, your 12 Mini Victorian Sponge Cakes placed before them.")
        print("Paul eyes them, then you, never showing any emotion.")
        print("'Right then, let's try them.', Mr. Hollywood states")
        print("He takes and hands it to Prue and takes one for himself.")
        print("There's silence. You can hear your heart beating in your chest...\n")
        print("Paul beckons you to come forth. You do so nervously.")
        print("Unexpectedly, he sticks his hand out. Yes, you receive the coveted Hollywood handshake!")
        print("'I can't find a fault with them. They're baked absolutely perfect.' Mr. Hollywood states.")
        print("Prue chimes in, 'They're absolutely scrumptious. I could eat them all.'\n")
        print("You did it! You baked a perfect 12 Mini Victorian Sponge Cakes,")
        print("and made Paul and Prue proud.")
        print("But then, in all of the excitement, everything goes dark...\n")
        print("You wake up on your kitchen floor, head pounding.")
        print(
            "It seems that you hit your head and knocked yourself out. You stand up slowly.")
        print("On the counter you see a tray of Mini Victorian Sponge Cakes... But only 10 remain...\n")
        print("Thanks for playing the Great British Bake Off Text Adventure Game!")

    else:
        print("You stand before Paul and Prue, your 12 Mini Victorian Sponge Cakes placed before them.")
        print("Paul eyes them, then you, never showing any emotion.")
        print("'Right then, let's try them.', Mr. Hollywood states")
        print("He takes and hands it to Prue and takes one for himself.")
        print("There's silence. You can hear your heart beating in your chest...\n")
        print("Paul takes a bite and finishes it before looking up at you.")
        print(
            "'It's underdone', he states.'It also seems as if you've missed an ingredient.'")
        print("Prue chimes in, 'This is quite a shame... I was really looking forward to these.'\n")
        print("You're crushed! You realized that you missed an ingredient. This lead to a bad bake.")
        print("You did it! You failed to bake perfect 12 Mini Victorian Sponge Cakes,")
        print("and Paul and Prue are disappointed.")
        print("But then, reeling in this defeat, everything goes dark...\n")
        print("You wake up on your kitchen floor, head pounding.")
        print(
            "It seems that you hit your head and knocked yourself out. You stand up slowly.")
        print("On the counter you see a tray of Mini Victorian Sponge Cakes... But only 10 remain...\n")
        print("Thanks for playing the Great British Bake Off Text Adventure Game!")


# def endGame takes in inventory list. sorts and checks to see if player has all necessary items against
# requiredItems. If player does, they win. If they don't, Paul Hollywood will be upset (player loses)


def endGame(list):

    requiredItems = ['500g strawberries', '175g castor sugar', 'Icing sugar', '500g jam sugar', '300ml double cream',
                     '175g unsalted butter', '175g self-raising flour', '3 large eggs', '1tsp vanilla extract']
    # sort both lists for comparison
    requiredItems.sort()
    list.sort()

    if list == requiredItems:
        endGameText(True)
        # print(True)
    else:
        endGameText(False)
        # print(False)


def endGameText(bool):
    if bool == True:
        print("Win")
    elif bool == False:
        print("Fail")

# def gameEngine acts as the game engine/logic. contains loop for continues gameplay until
# player enters the kitchen where the boss is located. at this point (gameEngine) calls the endGame
# and passes inventory list


def gameEngine():
    # reference list for directions commands
    direction = ['North', 'South', 'East', 'West']
    # starting position for player
    currentRoom = 'Vestibule'
    # player inventory
    inventory = []
    # game loop. remains true unless player enters kitchen, then breaks.
    while True:
        print("------------------------------")
        # current room
        print(f"You are in the {currentRoom}")
        # current inventory
        print("Inventory = ", inventory)
        # if item key not empty, show value
        if rooms[currentRoom]['item'] != '':
            print('You see', rooms[currentRoom]['item'])
        print("------------------------------")
        # break loop if kitchen entered
        if currentRoom == 'Kitchen':
            endGame(inventory)
            break
        # take player input
        user_input = input("Enter your move:\n")
        # grab last index to compare for direction
        direction = user_input.split(' ')[-1]
        # split for grab item functionality
        grab = user_input.split(' ')
        # join list grab to string food
        food = ' '.join(grab[1:])
        # if user enters grab command
        if user_input.split(' ')[0] == 'grab':
            # check if item requested exists in currentRoom
            if food in rooms[currentRoom]['item']:
                # grab item and append to inventory. print result
                inventory.append(rooms[currentRoom]['item'])
                print("You picked up", rooms[currentRoom]['item'])
                # set that item value to empty
                rooms[currentRoom]['item'] = ''
            else:
                print("You can't get", user_input)
        # check if direction command exists from currentRoom in rooms
        elif direction in rooms[currentRoom]:
            # if it does, change currentRoom
            currentRoom = rooms[currentRoom][direction]
        # elif direction not available, tell player that direction is not
        # available or invalid input
        elif direction not in rooms[currentRoom]:
            if direction in direction:
                print("You can't go that way!")
            else:
                print("Invalid move!")


# def main function. Calls greeting, instructions, and gameEngine functions.

def main():
    # call greeting function
    greeting()
    # call instruction function
    instructions()
    # while loop set to True to continue loop
    gameEngine()
    # print(gameEngine())


# call def main(), start program.
main()
