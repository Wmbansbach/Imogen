import databank

class Player:
    """description of class"""

    ## use list to transfer variables instead?
    def __init__(self, name, level, hitpoints, strength,
                 agility, critical, intelligence, exp, mana):

        # Primary Stats
        self.name = name
        self.level = level
        self.hitpoints = hitpoints
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.critical = critical
        self.exp = exp
        self.mana = mana

        # Dictionary Creation call
        self.dictList = []
        self.createDicts()

    def createDicts(self):
        self.charDict = {"name": self.name, "level": self.level,
                          "hitpoints": self.hitpoints, "strength": self.strength,
                          "agility": self.agility, "intelligence": self.intelligence,
                          "experience": self.exp, "mana": self.mana,
                          "critical": self.critical
                          }

        self.itemDict = {"Health Potion": 0,
                          "Energy Potion": 0,
                          "Food": [],
                          "Drinks": [],
                          "Armour": databank.armourDict["a1"],
                          "Weapon": None
                          }

        self.progressDict = {"Level_1": False,
                              "Level_2": False,
                              "Level_3": False
                              }
        self.dictList.append(self.charDict)
        self.dictList.append(self.itemDict)
        self.dictList.append(self.progressDict)

    def useHealthPotion(self):
        if self.dictList[1]["Health Potion"] != 0:
            self.hitpoints += 10
            self.dictList[1]["Health Potion"] -= 1
        else:
            print("You cannot do that...")

    def useManaPotion(self):
        if self.dictList[1]["Energy Potion"] != 0:
            self.mana += 15
            self.dictList[1]["Energy Potion"] -= 1
        else:
            print("You cannot do that...")


class Enemy:
    def __init__(self, name, race, level, hitpoints,
                 strength, agility, intellegence):
        # Primary Stats
        self.name = name
        self.race = race
        self.level = level
        self.hitpoints = hitpoints
        self.strength = strength
        self.agility = agility
        self.intellegence = intellegence
        pass
