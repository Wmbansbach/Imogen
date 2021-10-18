import tools
import databank
from profiles import Player

class startMenu:
    def __init__(self):
        self.DisplayText()
        self.Update()

    def DisplayText(self):
        print("Welcome to Tales of Valor!\n")
        print("**********************************************************\n")
        print("*    WELCOME, ADVENTURER!")
        print("*    This is a text-based RPG in which you can")
        print("*    level a character, aquire gear, and finish quests!\n\n")
        print("**********************************************************\n")
        print("SELECT ONE OF THE FOLLOWING\n\n")
        print("1:\tNew Game\n")
        print("2:\tLoad Game\n")
        print("3:\tQuit\n\n")

    def Update(self):
        while True:
            try:
                choice = int(input("MAKE A SELECTION: "))
            except UnboundLocalError:
                print('Be sure to input a number...')
                continue
            except ValueError:
                print("Be sure to input something!")
                continue
            else:
                break
        if choice == 1:
            CreateCharacter()


        elif choice == 2:
            loadChar = tools.GameLoadCharacter()
            if not loadChar:
                CreateCharacter()

        elif choice == 3:
            tools.QuitGame()
            


class CreateCharacter:

    def __init__(self):
        self.name = self.cName()
        self.level = 0
        self.exp = 1
        self.hitpoints = 100
        self.mana = 100
        self.strength = 5
        self.intelligence = 12
        self.agility = 4
        self.critical = 3

        # creating character class
        newChar = Player(self.name, self.level, self.hitpoints, 
                         self.strength, self.agility, self.critical,
                         self.intelligence, self.exp, self.mana)

        # copy of dictionary saved to file with character inside
        databank.characterLib = newChar
        tools.SaveCharacter(newChar)
        self.newChar = newChar

    def cName(self):
        print("You have selected New Game!\n")
        print('Before we begin, lets create your Character!\n\n')

        tools.ManageDir()

        while True:
            self.name = input("First lets give your character a name: ")
            if not tools.DuplicateCheck(self.name):
                print('Your Character\'s name will be: ' + self.name + '.\n')
                keepname = input('Do you wish to keep this name?(yes/no): \n')
                if keepname.lower() == 'yes' or 'y':
                    return self.name
                else:
                    print('Re-input Name...\n\n')
                    continue
            else:
                print("There is a duplicate found...Please re-enter a name.")
                continue
