import databank
import tools

class Manager():
    """ Runs, Loads, and Updates game levels
    """
    
    def __init__(self):
        self.levelCounter, self.levelPosition = tools.ParseLevelDict()

        if not self.levelCounter and self.levelPosition:
            self.EndGame()

        elif self.levelCounter and self.levelPosition:
            self.levelPosition = "Level_1"
            self.levelCounter = 1
            self.RunGame()

        else:
            self.RunGame()

    def RunGame(self):
        while self.levelCounter < 4:
            self.LoadLevel()
            self.UpdateLevel()

    def LoadLevel(self):
        level = databank.levelsDict[self.levelPosition]
        level.Run()

    def UpdateLevel(self):
        databank.characterLib.progressDict[self.levelPosition] = True
        cutLevel = self.levelPosition[:-1]
        self.levelCounter += 1
        self.levelPosition = cutLevel + str(self.levelCounter)
        
    def EndGame(self):
        pass
