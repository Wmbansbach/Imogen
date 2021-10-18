import databank
import tools    
   

# Levels provide the base layer where the story will told

class Level1:

    
    def Run(self):
        self.player = databank.characterLib

        self.SectionOne()

    def SectionOne(self):
        
        print("Your name is " + self.player.name + ". You are a young Paladin of the Light.")
        tools.MoveOn()
        print("You have been sent to the Earthen Realm by the Vinar\n" +
              "to help Earthen beings fend off the Balnor.")


class Level2:
    # Level Init Method
    def Run(self):
        print("Level 2")
    
class Level3:
    def Run(self):
        print(databank.characterLib.progressDict)
