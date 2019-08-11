from turtle import Turtle
class playGame():

    def __init__(self):
        self.score = 0
        self.currentRoom = ""
        self.potionList = []
        self.eye = 0
        self.leg = 0
        self.wing = 0
        self.frog = 0
        self.hair = 0
        self.roomOneToThree = 0
        self.roomOneToSix = 0
        self.roomOneToEight = 0
        self.roomOneToFive = 0
        self.roomTwoToTwoWest = 0
        self.roomTwoToTwoSouth = 0
        self.roomTwoToThree = 0
        self.roomThreeToFour = 0
        self.roomThreeToOne = 0
        self.roomThreeToTwo = 0
        self.roomFourToSixEast = 0
        self.roomFourToSixSouth = 0
        self.roomFiveToSeven = 0
        self.roomFiveToOne = 0
        self.roomSixToEight = 0
        self.roomSixToNine = 0
        self.roomSixToOne = 0
        self.roomSixToFour = 0
        self.roomSevenToTwo = 0
        self.roomSevenToFive = 0
        self.roomEightToSix = 0
        self.roomNineToTen = 0
        self.roomNineToSix = 0
        self.roomTenToNine = 0
        self.roomOneCount = 0
        self.roomTwoCount = 0
        self.roomThreeCount = 0
        self.roomFourCount = 0
        self.roomFiveCount = 0
        self.roomSixCount = 0
        self.roomSevenCount = 0
        self.roomEightCount = 0
        self.roomNineCount = 0
        self.roomTenCount = 0
        self.roomOnePotionList = []
        self.roomTwoList = ["EYE OF NEWT"]
        self.roomThreeList = []
        self.roomFourList = ["LIZARD'S LEG"]
        self.roomFiveList = []
        self.roomSixList = []
        self.roomSevenList = ["TOE OF FROG"]
        self.roomEightList = ["OWLET'S WING"]
        self.roomNineList = []
        self.roomTenList = ["CAT HAIR"]
        self.difficultyLevel = ""   
        self.gameOptions()

    def gameOptions(self):
        options = int(input('''Welcome to the game "In The Middle, A Cauldron Boiling".
To win, you must find all five ingredients the witches need for their potion,
and then deliver them to the room the witches are in.  The commands to
be used are:

Draw: draws a map
Go (direction), move (direction), or (direction): used to travel
    - directions are north, south, east, and west
Take (item): adds the item to your inventory
Drop (item): drops the item to the room you are in
Inventory: displays all items currently in your inventory
Look: displays the room description
Score: displays your score
Quit: quits the game

Please choose your difficulty level:
1. Easy
2. Normal
3. Hard
'''))
        if options == 1:
            self.difficultyLevel = "Easy"
        elif options == 2:
            self.difficultyLevel = "Normal"
        else:
            self.difficultyLevel = "Hard"
        print('''
Thank you!  Enjoy the game!
''')
        self.roomOne()

    def roomOne(self):
        self.roomOneCount += 1
        print("You are in room one.")
        print('''
You are in a dark cave.  In the middle, there is a cauldron boiling.
With a clasp of thunder, three witches suddenly appear before you.
''')      
        if self.roomOneCount == 1:
            self.score += 1
            print('''The witches speak in unison:
"Mortal, we have summoned thee, make haste!
And go forth into the farrow'd waste.
Find eye of newt, and toe of frog,
And deliver thus to this Scottish bog.
Lizard's leg, and owlet's wing,
And hair of cat that used to sing.
These things we need t' brew our charm;
Bring them forth -and suffer no 'arm.
Leave us and go!
'Tis no more to be said,
Save if you fail, then thou be stricken, dead.
''')
        else:
            print('''The witches stand before you, glaring; they seem to be
exspecting something from you.
''')
        while True:
            if self.isWinner():
                print('''The witches look at your items with suspicion, but decide to go
through with the incantation of the spell:

"Take lizard's leg and owlet's wing,
And hair of cat that used to sing.
In the cauldron they all shall go;
Stirring briskly, to and fro.
When the color is of a hog,
Add eye of newt and toe of frog.
Bubble all i' the charmed pot;
Bubble all 'til good and hot.
Pour the broth into a cup of stone,
And stir it well with a mummy's bone.

You take the resulting broth offered to you and drink ...
As the fog clears, you find yourself at a computer terminal;
your adventure is at an end.
''')
                self.congrats()
            command = input("Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.score -+ 1
                self.roomOne()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomOnePotionList.append("CAT HAIR")
                    self.score += 1
                    print("CAT HAIR has been succesfully dropped to room one.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomOnePotionList.append("EYE OF NEWT")
                    self.score += 1
                    print("EYE OF NEWT has been successfully dropped to room one.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomOnePotionList.append("TOE OF FROG")
                    self.score += 1
                    print("TOE OF FROG has been successfully dropped to room one.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomOnePotionList.append("LIZARD'S LEG")
                    self.score += 1
                    print("LIZARD'S LEG has been successfully dropped to room one.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomOnePotionList.append("OWLET'S WING")
                    self.score += 1
                    print("OWLET'S WING has been successfully dropped to room one.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomOnePotionList:
                    self.roomOnePotionList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    self.score -= 1
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomOnePotionList:
                    self.roomOnePotionList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    self.score -= 1
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomOnePotionList:
                    self.roomOnePotionList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    self.score -= 1
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomOnePotionList:
                    self.roomOnePotionList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    self.score -= 1
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomOnePotionList:
                    self.roomOnePotionList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    self.score -= 1
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                self.roomOneToThree = 1
                self.roomThree()
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                self.roomOneToEight = 1
                self.roomEight()
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                self.roomOneToFive = 1
                self.roomFive()
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                self.roomOneToSix = 1
                self.roomSix()
            else:
                print("That is not a valid command for this room.")             
        
    def roomTwo(self):
        self.roomTwoCount += 1
        if self.roomTwoCount == 1:
            self.score += 1
        print("You are in room Two")
        print('''
You're transported back in time ... you find yourself in Georgia during
the midst of a congressional campaign.
''')
        if self.eye == 0:
            print('''There is a campaign poster of Newt Gingrich, the
Speaker of the House of Representatives, on the wall, with his large eyes looking right at you.
''')
        else: 
            print('''There is a defaced poster of Newt Gingrich on the wall.
''')
        while True:    
            command = input("Please Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomTwo()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomTwoList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room two.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomTwoList.append("EYE OF NEWT")
                    self.eye = 0
                    print("EYE OF NEWT has been successfully dropped to room two.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomTwoList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room two.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomTwoList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room two.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomTwoList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room two.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomTwoList:
                    self.roomTwoList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomTwoList:
                    self.roomTwoList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomTwoList:
                    self.roomTwoList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomTwoList:
                    self.roomTwoList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomTwoList:
                    self.roomTwoList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    self.eye = 1
                    print("You have added EYE OF NEWT to your inventory.")
                else:
                    print("You have already taken EYE OF NEWT from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                print("You bump into a wall. ")
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                print("You travel through a dark tunnel that winds around and brings you back to the same room. ")
                self.roomTwoToTwoSouth = 1
                self.roomTwo()
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                print("You travel through a dark tunnel that winds around and brings you back to the same room. ")
                self.roomTwoToTwoWest = 1
                self.roomTwo()
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                self.roomTwoToThree = 1
                self.roomThree()
            else:
                print("That is not a valid command for this room.")

    def roomThree(self):
        self.roomThreeCount += 1
        if self.roomThreeCount == 1:
            self.score += 1
        print('''You are in room three.

The first thing you notice upon entering this room is the overabundance of
sunshine and joy.  Everywhere you look, there is a young girl in a brightly flowing
dress, singing about true love's kiss and finding her prince.  With all the
sweetness in this room, you start feeling slightly nauseous and run for the
next door.
''')
        while True:    
            command = input("Please Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomThree()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomThreeList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room three.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomThreeList.append("EYE OF NEWT")
                    print("EYE OF NEWT has been successfully dropped to room three.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomThreeList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room three.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomThreeList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room three.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomThreeList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room three.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomThreeList:
                    self.roomThreeList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomThreeList:
                    self.roomThreeList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomThreeList:
                    self.roomThreeList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomThreeList:
                    self.roomThreeList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomThreeList:
                    self.roomThreeList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                print("You bump into a wall. ")
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                self.roomThreeToOne = 1
                self.roomOne()
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                self.roomThreeToTwo = 1
                self.roomTwo()
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                self.roomThreeToFour = 1
                self.roomFour()
            else:
                print("That is not a valid command for this room.")

    def roomFour(self):
        self.roomFourCount += 1
        if self.roomFourCount == 1:
            self.score += 1
        print("You are in room four.")
        if self.leg == 0:
            if self.wing == 0:
                print('''
The ceiling in this room is quite high and the walls are set many feet apart.
In the center of the room, there is a Jedi Knight battling a dragon who, upon close inspection, is
wearing a collar with the word Owlet written upon the nametag.  The dragon is currently circling the height
of the room.  As you stand transfixed, the dragon suddenly folds in its wings and dives toward the awaiting
Jedi.  Fire shoots from the dragon's mouth and engulfs the Jedi.  Or rather, it engulfs the space where the
Jedi had been standing only moments before, for now the Jedi, presumably using the Force, is astride the
dragon, holding his lightsaber high overhead.  The dragon screetches her ire and the Jedi makes a quick
downward slash, slicing one of the dragon's legs clean off.  Screaming in pain and fury, the dragon uses
a powerful spin manuever to shake the Jedi from her back, and then quickly heads for an exit.  The Jedi,
once again using the powers of the Force, lands softly and pursues.  The room is now empty, save for the
dragon's leg lying amidst a puddle of blood and the Jedi's scorched robe.
''')
            else:
                print('''
The ceiling in this room is quite high and the walls are set many feet apart.
In the center of the room, there is a Jedi Knight battling a dragon who, upon close inpection, is missing
a wing and wearing a collar with the word Owlet written upon the nametag.  The dragon is currently
circling the height of the room.  As you stand transfixed, the dragon suddenly folds in its wings and
dives toward the awaiting Jedi.  Fire shoots from the dragon's mouth and engulfs the Jedi.  Or rather, it
engulfs the space where the Jedi had been standing only moments before, for now the Jedi, presumably using
the Force, is astride the dragon, holding his lightsaber high overhead.  The dragon screetches her ire and
the Jedi makes a quick downward slash, slicing one of the dragon's legs clean off.  Screaming in pain and
fury, the dragon uses a powerful spin manuever to shake the Jedi from her back, and then quickly heads for
an exit.  The Jedi, once again using the powers of the Force, lands softly and pursues.  The room is now
empty, save for the dragon's leg lying amidst a puddle of blood and the Jedi's scorched robe.
''')
        else:
            print('''You seem to remember a great battle between a Jedi and a dragon taking place in this room.
''')          
        while True:    
            command = input("Please Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomFour()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomFourList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room four.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomFourList.append("EYE OF NEWT")
                    print("EYE OF NEWT has been successfully dropped to room four.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomFourList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room four.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomFourList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room four.")
                    self.leg = 0
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomFourList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room four.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomFourList:
                    self.roomFourList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomFourList:
                    self.roomFourList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomFourList:
                    self.roomFourList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomFourList:
                    self.roomFourList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                    self.leg = 1
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomFourList:
                    self.roomFourList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                print("You bump into a wall. ")
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                self.roomFourToSixSouth = 1
                self.roomSix()
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                print("You try to open the door to travel WEST but find that it is locked. ")
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                self.roomFourToSixEast = 1
                self.roomSix()
            else:
                print("That is not a valid command for this room.")

    def roomFive(self):
        self.roomFiveCount += 1
        if self.roomFiveCount == 1:
            self.score += 1
        print('''You are in room five.

The first thing you notice upon entering this room is the unashamed fear displayed by
grown men cowering in the dark spaces throughout.  The trembling in their bodies is so
fierce that the crowns atop their heads are slowly being shaken right off.  Amidst the
inconsistent "clangs" piercing the otherwise silent room, made as each crown encounters
the floor, you quietly tiptoe toward your exit of choice.
''')
        while True:    
            command = input("Please Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomFive()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomFiveList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room five.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomFiveList.append("EYE OF NEWT")
                    print("EYE OF NEWT has been successfully dropped to room five.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomFiveList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room five.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomFiveList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room five.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomFiveList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room five.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomFiveList:
                    self.roomFiveList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomFiveList:
                    self.roomFiveList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomFiveList:
                    self.roomFiveList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomFiveList:
                    self.roomFiveList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomFiveList:
                    self.roomFiveList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                print("You bump into a wall. ")
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                print("You bump into a wall. ")
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                self.roomFiveToSeven = 1
                self.roomSeven()
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                self.roomFiveToOne = 1
                self.roomOne()
            else:
                print("That is not a valid command for this room.")

    def roomSix(self):
        self.roomSixCount += 1
        if self.roomSixCount == 1:
            self.score += 1
        print("You are in room six.")
        if self.wing == 1:
            if self.leg == 1:
                print('''
In the center of the room is a huge nest filled with jewels and gold.  If not for the
many bones surrounding the nest, not to mention the dragon with the missing wing and leg
apparently recovering in the middle of it, you would be tempted to take a handful for yourself.
As it is, you best be on your way before the creature that calls this nest "home" realizes
she has company.
''')
        else:
            print('''
In the center of the room is a huge nest filled with jewels and gold.  If not for the
many bones surrounding the nest, you would be tempted to take a handful for yourself.
As it is, you best be on your way before the creature that calls this nest "home" comes
back.
''')
        while True:    
            command = input("Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomSix()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomSixList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room six.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomSixList.append("EYE OF NEWT")
                    print("EYE OF NEWT has been successfully dropped to room six.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomSixList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room six.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomSixList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room six.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomSixList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room six.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomSixList:
                    self.roomSixList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomSixList:
                    self.roomSixList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomSixList:
                    self.roomSixList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomSixList:
                    self.roomSixList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomSixList:
                    self.roomSixList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                self.roomSixToFour = 1
                self.roomFour()
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                self.roomSixToEight = 1
                self.roomEight()
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                self.roomSixToOne = 1
                self.roomOne()
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                self.roomSixToNine = 1
                self.roomNine()
            else:
                print("That is not a valid command for this room.")

    def roomSeven(self):
        self.roomSevenCount += 1
        if self.roomSevenCount == 1:
            self.score += 1
        print("You are in room seven.")
        if self.frog == 0:
            print('''
You find yourself walking into a scene where the cast of Monty
Python's Flying Circus is performing the "Crunchy Frog" sketch.  You
see the confectioner as he replies, "If we took the bones out it
wouldn't be crunchy now, would it?" You see a box of "Crunchy Frog"
chocolates, the contents of which contains a dozen nicely cleaned
whole frogs that have been carefully hand-dipped in the finest
chocolate.
''')
        else:
            print('''
The Monty Python crew has moved on to reinacting a scene from the Holy Grail.
The Green Knight and the Black Knight seemed to be locked in a very important
battle.  The Black Knight is down to one leg and is hopping around on it,
trying to prevent the Green Knight from crossing the river by way of the bridge,
which consists of a single plank of wood connecting both banks of a tiny stream.
As the Black Knight continues to valiantly stand his guard, you step across
the trickle of flowing water and make your way to the exit.
''')
        while True:    
            command = input("Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomSeven()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomSevenList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room seven.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomSevenList.append("EYE OF NEWT")
                    print("EYE OF NEWT has been successfully dropped to room seven.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomSevenList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room seven.")
                    self.frog = 0
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomSevenList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room seven.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomSevenList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room seven.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomSevenList:
                    self.roomSevenList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomSevenList:
                    self.roomSevenList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomSevenList:
                    self.roomSevenList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                    self.frog = 1
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomSevenList:
                    self.roomSevenList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomSevenList:
                    self.roomSevenList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                self.roomSevenToTwo = 1
                self.roomTwo()
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                print("You bump into a wall. ")
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                self.roomSevenToFive = 1
                self.roomFive()
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                print("You bump into a wall")
            else:
                print("That is not a valid command for this room.")

    def roomEight(self):
        self.roomEightCount += 1
        if self.roomEightCount == 1:
            self.score += 1
        if self.wing == 0:
            if self.leg == 0:
                print('''You are in room eight.

This room is vast in size and has amazing accoustics, made apparent by the impressive echoes of a great battle
happening before your eyes.  A young boy with a stick in his hand is facing off with a fearsome dragon, whose
name, going by the collar around her neck, is Owlet. As the dragon begins her decent from near the ceiling of
the room, the boy shouts "Accio Firebolt!"  From the doorway behind you, a broom suddenly whooshes through the
air, barely missing you, and heads straight for the boy's outstretched hand.  The boy (is that a scar on his
forehead?) mounts the broom and barely escapes the ensuing spout of fire, courtesy of the dragon.  As the pair
loop and dive around the room, the dragon eventually seems to tire.  Taking advantage of this, the boy pulls a
miraculous manuever that puts him right above the momentarily confused dragon.  With a sudden cry of "Sectumsempra!"
the boy slashes his stick toward the dragon, and in fact, slashes the dragon's wing right off.  With a cry of
pain and fury, the dragon falls to the floor and scurries to the exit, the boy hot on her heels.  The room is
now void, save for the severed wing lying on the floor.
''')
            else:
                print('''You are in room eight.

This room is vast in size and has amazing accoustics, made apparent by the impressive echoes of a great battle
happening before your eyes.  A young boy with a stick in his hand is facing off with a fearsome dragon with a
missing leg, whose name, going by the collar around her neck, is Owlet.  As the dragon begins her decent from
near the ceiling of the room, the boy shouts "Accio Firebolt!"  From the doorway behind you, a broom suddenly
whooshes through the air, barely missing you, and heads straight for the boy's outstretched hand.  The boy (is
that a scar on his forehead?) mounts the broom and barely escapes the ensuing spout of fire, courtesy of the dragon.
As the pair loop and dive around the room, the dragon eventually seems to tire.  Taking advantage of this, the boy
pulls a miraculous manuever that puts him right above the momentarily confused dragon.  With a sudden cry of
"Sectumsempra!" the boy slashes his stick toward the dragon, and in fact, slashes the dragon's wing right off.
With a cry of pain and fury, the dragon falls to the floor and scurries to the exit, the boy hot on her heels.
The room is now void, save for the severed wing lying on the floor.
''')
        else:
            print('''You are in room eight.

You seem to remember picking up Owlet's wing from this room earlier.
''')
        while True:    
            command = input("Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomEight()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomEightList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room eight.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomEightList.append("EYE OF NEWT")
                    print("EYE OF NEWT has been successfully dropped to room eight.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomEightList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room eight.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomEightList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room eight.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomEightList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room eight.")
                    self.wing = 0
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomEightList:
                    self.roomEightList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomEightList:
                    self.roomEightList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomEightList:
                    self.roomEightList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomEightList:
                    self.roomEightList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomEightList:
                    self.roomEightList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                    self.wing = 1
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                print("You bump into a wall. ")
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                print("You bump into a wall. ")
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                print("You try to open the door to travel WEST but find that it is locked. ")
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                self.roomEightToSix = 1
                self.roomSix()
            else:
                print("That is not a valid command for this room.")

    def roomNine(self):
        self.roomNineCount += 1
        if self.roomNineCount == 1:
            self.score += 1
            print("You are in room nine.")
            print('''
As you step through the time portal, your head begins to spin you're
disoriented and then awaken.  You find yourself at the outside door of
a dormitory kitchen.  Listening, you hear the Chef yelling, "Stop!
Stop!" while several cats inside are singing a serenade of the "Meow
Mix" commercial theme.  Suddently, the repeated thump of a cleaver puts
an abrupt end to the music.
''')
        else:
            print('''You are in room nine.

Where it was once filled with music in the form of cats meowing, it is now silent.  You find yourself humming
the theme to the Meow Mix commercial as you ponder your next move.
''')
        while True:    
            command = input("Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomNine()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomNineList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room nine.")
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomNineList.append("EYE OF NEWT")
                    print("EYE OF NEWT has been successfully dropped to room nine.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomNineList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room nine.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomNineList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room nine.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomNineList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room nine.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomNineList:
                    self.roomNineList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomNineList:
                    self.roomNineList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomNineList:
                    self.roomNineList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomNineList:
                    self.roomNineList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomNineList:
                    self.roomNineList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                self.roomNineToSix = 1
                self.roomSix()
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                print("You bump into a wall. ")
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                self.roomNineToTen = 1
                self.roomTen()
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                print("You bump into a wall")
            else:
                print("That is not a valid command for this room.")

    def roomTen(self):
        self.roomTenCount += 1
        if self.roomTenCount == 1:
            self.score += 1
        print("You are in room Ten.")
        if self.hair == 0:
            print('''
You are in the kitchen.  Looking out into the cafeteria, you see
students reaching for Pepto-Bismol while trying to stomach the latest
version of the Chef's Surprise.  You see the Chef as he finishes
dumping fresh meat into his 50-quart stewing pot.  There are clumps of
cat hair on the butcher's block.  You hear the Chef muttering to
himself, "Prepared properly, cat tastes much like chicken ...
''')
        else:
            print('''The cafeteria is now void of all students.  They were, however, gracious
enough to leave behind faint traces of vomit wafting through the air.  Trying to steady your
rebelling stomache, you turn your eyes to the kitchen.  This proves to be a mistake, however,
for one glimpse of the still-bloody butcher's block has you immediately adding to the aroma.  I think it
would be best if you hurried along ...
''')
        while True:    
            command = input("Please enter a command. ").upper()
            if command == "DRAW":
                self.drawMap()
            elif command == "QUIT":
                quit()
            elif command == "LOOK":
                self.roomTen()
            elif command == "INVENTORY":
                count = 1
                if self.potionList == []:
                    print("There is nothing in your inventory.")
                else:
                    for i in self.potionList:
                        print(str(count) + ". " + str(i))
                        count += 1
            elif command == "SCORE":
                print(self.score)
            elif command == "DROP HAIR":
                if "CAT HAIR" in self.potionList:
                    self.potionList.remove("CAT HAIR")
                    self.roomTenList.append("CAT HAIR")
                    print("CAT HAIR has been succesfully dropped to room ten.")
                    self.hair = 0
                else:
                    print("You do not have a CAT HAIR to drop.")
            elif command == "DROP EYE":
                if "EYE OF NEWT" in self.potionList:
                    self.potionList.remove("EYE OF NEWT")
                    self.roomTenList.append("EYE OF NEWT")
                    print("EYE OF NEWT has been successfully dropped to room ten.")
                else:
                    print("You do not have an EYE OF NEWT to drop.")
            elif command == "DROP TOE" or command == "DROP FROG":
                if "TOE OF FROG" in self.potionList:
                    self.potionList.remove("TOE OF FROG")
                    self.roomTenList.append("TOE OF FROG")
                    print("TOE OF FROG has been successfully dropped to room ten.")
                else:
                    print("You do not have a TOE OF FROG to drop.")
            elif command == "DROP LEG":
                if "LIZARD'S LEG" in self.potionList:
                    self.potionList.remove("LIZARD'S LEG")
                    self.roomTenList.append("LIZARD'S LEG")
                    print("LIZARD'S LEG has been successfully dropped to room ten.")
                else:
                    print("You do not have a LIZARD'S LEG to drop.")
            elif command == "DROP WING":
                if "OWLET'S WING" in self.potionList:
                    self.potionList.remove("OWLET'S WING")
                    self.roomTenList.append("OWLET'S WING")
                    print("OWLET'S WING has been successfully dropped to room ten.")
                else:
                    print("You do not have an OWLET'S WING to drop.")
            elif command == "TAKE HAIR":
                if "CAT HAIR" in self.roomTenList:
                    self.roomTenList.remove("CAT HAIR")
                    self.potionList.append("CAT HAIR")
                    print("You have taken CAT HAIR from the room and added it to your inventory.")
                    self.hair = 1
                else:
                    print("There is no CAT HAIR to take from this room.")
            elif command == "TAKE EYE":
                if "EYE OF NEWT" in self.roomTenList:
                    self.roomTenList.remove("EYE OF NEWT")
                    self.potionList.append("EYE OF NEWT")
                    print("You have taken EYE OF NEWT from the room and added it to your inventory.")
                else:
                    print("There is no EYE OF NEWT to take from this room.")
            elif command == "TAKE TOE" or command == "TAKE FROG":
                if "TOE OF FROG" in self.roomTenList:
                    self.roomTenList.remove("TOE OF FROG")
                    self.potionList.append("TOE OF FROG")
                    print("You have taken TOE OF FROG from the room and added it to your inventory.")
                else:
                    print("There is no TOE OF FROG to take from this room.")
            elif command == "TAKE LEG":
                if "LIZARD'S LEG" in self.roomTenList:
                    self.roomTenList.remove("LIZARD'S LEG")
                    self.potionList.append("LIZARD'S LEG")
                    print("You have taken LIZARD'S LEG from the room and added it to your inventory.")
                else:
                    print("There is no LIZARD'S LEG to take from this room.")
            elif command == "TAKE WING":
                if "OWLET'S WING" in self.roomTenList:
                    self.roomTenList.remove("OWLET'S WING")
                    self.potionList.append("OWLET'S WING")
                    print("You have taken OWLET'S WING from the room and added it to your inventory.")
                else:
                    print("There is no OWLET'S WING to take from this room.")
            elif command == "MOVE NORTH" or command == "GO NORTH" or command == "NORTH":
                print("You bump into a wall. ")
            elif command == "MOVE SOUTH" or command == "GO SOUTH" or command == "SOUTH":
                print("You bump into a wall. ")
            elif command == "MOVE WEST" or command == "GO WEST" or command == "WEST":
                print("You bump into a wall. ")
            elif command == "MOVE EAST" or command == "GO EAST" or command == "EAST":
                self.roomTenToNine = 1
                self.roomNine()
            else:
                print("That is not a valid command for this room.")

    def isWinner(self):
        if "CAT HAIR" in self.roomOnePotionList and "EYE OF NEWT" in self.roomOnePotionList and "TOE OF FROG" in self.roomOnePotionList and "LIZARD'S LEG" in self.roomOnePotionList and "OWLET'S WING" in self.roomOnePotionList:
            return True
        return False
    def congrats(self):
        print("Congratulations, you have won the game!!  Your score is " + str(self.score) + ".")
        while True:
            playAgain = int(input('''Would you like to play again?  Please enter a number:
1. Yes
2. No
'''))
            if playAgain == 1:
                playGame()
            elif playAgain == 2:
                quit()
            else:
                print("That is not a valid entry.")

    def drawMap(self):
        if self.difficultyLevel != "Hard":
            t = Turtle()
            t.pensize(4)
            t.speed(10)
            t.circle(30)
            t.penup()
            t.goto(0, 50)
            t.pendown()
            t.goto(0,10)
            t.penup()

            if self.roomOneToThree > 0 or self.difficultyLevel == "Easy":
                t.goto(0, 60)
                t.setheading(90)
                t.pendown()
                t.goto(0, 200)
                t.setheading(315)
                t.forward(20)
                t.goto(0, 200)
                t.setheading(215)
                t.forward(20)
                t.penup()
                
            if self.roomOneToSix > 0 or self.difficultyLevel == "Easy":
                t.goto(30, 30)
                t.setheading(0)
                t.pendown()
                t.goto(170, 30)
                t.setheading(135)
                t.forward(20)
                t.goto(170, 30)
                t.setheading(225)
                t.forward(20)
                t.penup()

            if self.roomOneToEight > 0 or self.difficultyLevel == "Easy":
                t.goto(0, 0)
                t.setheading(270)
                t.pendown()
                t.forward(40)
                t.circle(30, 90)
                t.goto(70, -70)
                t.setheading(135)
                t.forward(20)
                t.goto(70, -70)
                t.setheading(225)
                t.forward(20)
                t.penup()

            if self.roomOneToFive > 0 or self.difficultyLevel == "Easy":
                t.goto(-30, 30)
                t.pendown()
                t.goto(-270, 30)
                t.setheading(45)
                t.forward(20)
                t.goto(-270, 30)
                t.setheading(315)
                t.forward(20)
                t.penup()

            if self.roomTwoCount > 0 or self.difficultyLevel == "Easy":
                t.goto(-200, 200)
                t.setheading(0)
                t.pendown()
                t.circle(30)
                t.penup()
                t.goto(-210, 240)
                t.setheading(90)
                t.pendown()
                t.circle(-10, 180)
                t.goto(-210, 210)
                t.goto(-190, 210)
                t.penup()

            if self.roomTwoToTwoWest > 0 or self.difficultyLevel == "Easy":
                t.goto(-230, 230)
                t.setheading(180)
                t.pendown()
                t.forward(15)
                t.circle(45, 270)
                t.goto(-200, 200)
                t.setheading(225)
                t.forward(20)
                t.goto(-200, 200)
                t.setheading(315)
                t.forward(20)
                t.penup()

            if self.roomTwoToTwoSouth > 0 or self.difficultyLevel == "Easy":
                t.goto(-230, 230)
                t.setheading(180)
                t.pendown()
                t.forward(15)
                t.circle(45, 270)
                t.goto(-200, 200)
                t.penup()
                t.goto(-230, 230)
                t.pendown()
                t.setheading(135)
                t.forward(20)
                t.goto(-230, 230)
                t.setheading(225)
                t.forward(20)
                t.penup()

            if self.roomTwoToThree > 0 or self.difficultyLevel == "Easy":
                t.goto(-170, 230)
                t.setheading(0)
                t.pendown()
                t.goto(-30, 230)
                t.setheading(125)
                t.forward(20)
                t.goto(-30, 230)
                t.setheading(225)
                t.forward(20)
                t.penup()

            if self.roomThreeCount > 0 or self.difficultyLevel == "Easy":
                t.goto(0, 200)
                t.setheading(0)
                t.pendown()
                t.circle(30)
                t.penup()
                t.goto(-10, 240)
                t.setheading(90)
                t.pendown()
                t.circle(-10, 270)
                t.setheading(0)
                t.circle(-10, 270)
                t.penup()

            if self.roomThreeToFour > 0 or self.difficultyLevel == "Easy":
                t.goto(30, 230)
                t.pendown()
                t.goto(170, 230)
                t.setheading(125)
                t.forward(20)
                t.goto(170, 230)
                t.setheading(235)
                t.forward(20)
                t.penup()

            if self.roomThreeToOne > 0 or self.difficultyLevel == "Easy":
                t.goto(0, 170)
                t.pendown()
                t.goto(0, 60)
                t.setheading(45)
                t.forward(20)
                t.goto(0, 60)
                t.setheading(135)
                t.forward(20)
                t.penup()

            if self.roomThreeToTwo > 0 or self.difficultyLevel == "Easy":
                t.goto(-30, 230)
                t.pendown()
                t.goto(-170, 230)
                t.setheading(45)
                t.forward(20)
                t.goto(-170, 230)
                t.setheading(315)
                t.forward(20)
                t.penup()
                
            if self.roomFourCount > 0 or self.difficultyLevel == "Easy":
                t.goto(200, 200)
                t.setheading(0)
                t.pendown()
                t.circle(30)
                t.penup()
                t.goto(190, 250)
                t.pendown()
                t.setheading(270)
                t.forward(20)
                t.setheading(0)
                t.forward(20)
                t.setheading(90)
                t.forward(20)
                t.setheading(270)
                t.forward(40)
                t.penup()

            if self.roomFourToSixEast > 0 or self.difficultyLevel == "Easy":
                t.goto(230, 230)
                t.setheading(0)
                t.pendown()
                t.forward(20)
                t.circle(-20, 130)
                t.goto(220, 50)
                t.setheading(45)
                t.forward(20)
                t.goto(220, 50)
                t.setheading(90)
                t.forward(20)
                t.penup()
                
            if self.roomFourToSixSouth > 0 or self.difficultyLevel == "Easy":
                t.goto(200, 200)
                t.setheading(270)
                t.pendown()
                t.goto(200, 60)
                t.setheading(45)
                t.forward(20)
                t.goto(200, 60)
                t.setheading(135)
                t.forward(20)
                t.penup()

            if self.roomFiveCount > 0 or self.difficultyLevel == "Easy":
                t.goto(-300, 0)
                t.pendown()
                t.setheading(0)
                t.circle(30)
                t.penup()
                t.goto(-290, 50)
                t.pendown()
                t.setheading(180)
                t.forward(20)
                t.setheading(270)
                t.forward(20)
                t.setheading(0)
                t.forward(10)
                t.circle(-10, 180)
                t.forward(10)
                t.penup()

            if self.roomFiveToSeven > 0 or self.difficultyLevel == "Easy":
                t.goto(-330, 30)
                t.setheading(180)
                t.pendown()
                for i in range(20):
                    t.forward(7)
                    t.circle(9, 10)
                t.goto(-130, -70)
                t.setheading(135)
                t.forward(20)
                t.goto(-130, -70)
                t.setheading(225)
                t.forward(20)
                t.penup()

            if self.roomFiveToOne > 0 or self.difficultyLevel == "Easy":
                t.goto(-270, 30)
                t.setheading(0)
                t.pendown()
                t.goto(-30, 30)
                t.setheading(135)
                t.forward(20)
                t.goto(-30, 30)
                t.setheading(225)
                t.forward(20)
                t.penup()
                
            if self.roomSixCount > 0 or self.difficultyLevel == "Easy":
                t.goto(200, 0)
                t.setheading(0)
                t.pendown()
                t.circle(30)
                t.penup()
                t.goto(210, 40)
                t.pendown()
                t.setheading(90)
                t.circle(10, 180)
                t.forward(20)
                t.setheading(270)
                t.circle(10)
                t.penup()

            if self.roomSixToEight > 0 or self.difficultyLevel == "Easy":
                t.goto(200, 0)
                t.setheading(270)
                t.pendown()
                t.forward(40)
                t.circle(-30, 90)
                t.goto(130, -70)
                t.setheading(45)
                t.forward(20)
                t.goto(130, -70)
                t.setheading(315)
                t.forward(20)
                t.penup()

            if self.roomSixToNine > 0 or self.difficultyLevel == "Easy":
                t.goto(230, 30)
                t.setheading(0)
                t.pendown()
                t.forward(30)
                t.circle(-40, 90)
                t.goto(300, -240)
                t.setheading(45)
                t.forward(20)
                t.goto(300, -240)
                t.setheading(135)
                t.forward(20)
                t.penup()

            if self.roomSixToOne > 0 or self.difficultyLevel == "Easy":
                t.goto(170, 30)
                t.setheading(180)
                t.pendown()
                t.goto(30, 30)
                t.setheading(45)
                t.forward(20)
                t.goto(30, 30)
                t.setheading(315)
                t.forward(20)
                t.penup()

            if self.roomSixToFour > 0 or self.difficultyLevel == "Easy":
                t.goto(200, 60)
                t.pendown()
                t.goto(200, 200)
                t.setheading(225)
                t.forward(20)
                t.goto(200, 200)
                t.setheading(315)
                t.forward(20)
                t.penup()
                
            if self.roomSevenCount > 0 or self.difficultyLevel == "Easy":
                t.goto(-100, -100)
                t.setheading(0)
                t.pendown()
                t.circle(30)
                t.penup()
                t.goto(-110, -55)
                t.pendown()
                t.setheading(0)
                t.forward(20)
                t.goto(-100, -90)
                t.penup()

            if self.roomSevenToTwo > 0 or self.difficultyLevel == "Easy":
                t.goto(-100, -40)
                t.pendown()
                t.setheading(90)
                t.forward(100)
                t.circle(20, 45)
                t.goto(-180, 210)
                t.setheading(270)
                t.forward(20)
                t.goto(-180, 210)
                t.setheading(0)
                t.forward(20)
                t.penup()

            if self.roomSevenToFive > 0 or self.difficultyLevel == "Easy":
                t.goto(-330, 30)
                t.setheading(180)
                t.pendown()
                for i in range(20):
                    t.forward(7)
                    t.circle(9, 10)
                t.goto(-130, -70)
                t.setheading(135)
                t.forward(20)
                t.goto(-130, -70)
                t.setheading(225)
                t.forward(20)
                t.penup()
                t.goto(-330, 30)
                t.pendown()
                t.setheading(135)
                t.forward(20)
                t.goto(-330, 30)
                t.setheading(225)
                t.forward(20)
                t.penup()

            if self.roomEightCount > 0 or self.difficultyLevel == "Easy":
                t.goto(100, -100)
                t.setheading(0)
                t.pendown()
                t.circle(30)
                t.penup()
                t.goto(100, -70)
                t.pendown()
                t.setheading(0)
                t.circle(10)
                t.circle(-10)
                t.penup()

            if self.roomEightToSix > 0 or self.difficultyLevel == "Easy":
                t.goto(200, 0)
                t.setheading(270)
                t.pendown()
                t.forward(40)
                t.circle(-30, 90)
                t.goto(130, -70)
                t.penup()
                t.goto(200, 0)
                t.pendown()
                t.setheading(225)
                t.forward(20)
                t.goto(200, 0)
                t.setheading(315)
                t.forward(20)
                t.penup()

            if self.roomNineCount > 0 or self.difficultyLevel == "Easy":
                t.goto(300, -300)
                t.setheading(0)
                t.pendown()
                t.circle(30)
                t.penup()
                t.goto(300, -270)
                t.setheading(0)
                t.pendown()
                t.circle(10)
                t.penup()
                t.goto(310, -260)
                t.setheading(270)
                t.pendown()
                t.forward(20)
                t.circle(-10, 180)
                t.penup()

            if self.roomNineToTen > 0 or self.difficultyLevel == "Easy":
                t.goto(270, -270)
                t.pendown()
                t.goto(30, -270)
                t.setheading(45)
                t.forward(20)
                t.goto(30, -270)
                t.setheading(315)
                t.forward(20)
                t.penup()

            if self.roomNineToSix > 0 or self.difficultyLevel == "Easy":
                t.goto(230, 30)
                t.setheading(0)
                t.pendown()
                t.forward(30)
                t.circle(-40, 90)
                t.goto(300, -240)
                t.penup()
                t.goto(230, 30)
                t.pendown()
                t.setheading(45)
                t.forward(20)
                t.goto(230, 30)
                t.setheading(315)
                t.forward(20)
                t.penup()
                
            if self.roomTenCount > 0 or self.difficultyLevel == "Easy":
                t.goto(0, -300)
                t.setheading(0)
                t.pendown()
                t.circle(30)
                t.penup()
                t.goto(-10, -250)
                t.pendown()
                t.setheading(270)
                t.forward(40)
                t.penup()
                t.goto(10, -250)
                t.setheading(0)
                t.pendown()
                t.circle(-10, 90)
                t.setheading(270)
                t.forward(20)
                t.circle(-10, 180)
                t.setheading(90)
                t.forward(20)
                t.circle(-10, 90)
                t.penup()

            if self.roomTenToNine > 0 or self.difficultyLevel == "Easy":
                t.goto(30, -270)
                t.pendown()
                t.goto(270, -270)
                t.setheading(135)
                t.forward(20)
                t.goto(270, -270)
                t.setheading(225)
                t.forward(20)
                t.penup()

playGame()
