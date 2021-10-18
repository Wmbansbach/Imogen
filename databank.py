import levels
import profiles

infoDict = {"elf": "Elf Info",
            "human": "Human Info",
            "orc": "Orc Info",
            "gnome": "Gnome Info",
            "mage": "Mage Info",
            "warrior": "Warrior Info",
            "ranger": "Ranger Info"
            }

# Temporary Character Variables
characterLib = None
loadNameList = []

enemiesDict = { "L1": 'Enemy'
                }


armourDict = {"a1": {"name": None, "armor": None,
                      "defense bonus": None, "description": None
                      }
               }

weaponDict = {"w1": {"name": None, "armor": None,
                      "defense bonus": None, "description": None
                      }
               }



levelsDict = {"Level_1": levels.Level1(),
          "Level_2": levels.Level2(),
          "Level_3": levels.Level3()
          }
