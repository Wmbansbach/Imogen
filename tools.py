import os
import sys
import pickle
import time
import databank

def Find_Data_File(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)

def GetDateTime():
    """
    |    GetDateTime:
    |    Function that returns formatted date and time
    """ 
    return time.strftime("__%m-%d-%Y", time.localtime())

def ManageDir(inGamesave = False):
    """
    |   Manage Directory:
    |   Function searches Saved Character file,
    |   if directory is populated, each name is truncated
    |   and added to list for further use, else is returns False
    """
    dirPath = FindDataFile("Saved_Characters")

    try:
        os.chdir(dirPath)
    except FileNotFoundError:
        os.mkdir(dirPath)
        os.chdir(dirPath)

    dirList = os.listdir(dirPath)

    if not dirList:
        return False
    else:
        if not inGamesave:
            for ind in dirList:
                indList = ind.split("__")
                databank.loadNameList.append(indList[0])
        else:
            fileList = []
            for ind in dirList:
                fileList.append(ind)

            return fileList

def DuplicateCheck(name):
    """
    |   Duplicate_Check:
    |   Simple function that parses pre-created
    |   name list to see if duplicates exist
    """
    duplicateCounter = 0
    isDuplicate = False

    for ind in databank.loadNameList:
        if name != ind:
            pass
        else:
            duplicateCounter += 1
    if duplicateCounter != 0:
        isDuplicate = True

    return isDuplicate


def MoveOn():
    print("\nPress enter to move on...")
    input()

def ParseLevelDict():
    """
    |   ParseLevelDict: 
    |   Parses the levelDictionary within the databank module.
    |   Ensures that the most current level is loaded from the characters saved file.
    """

    levelList = []
    levelBuffer = databank.characterLib.progressDict
    
    for level in levelBuffer:

        if levelBuffer[level]:
            levelList.append(level)

    # if the list is empty return True for a new character
    # if the list is full return False for a finished game
    # if the character is still progressing, return a levelCounter and 
    # current start level position
    if len(levelList) == 0:
        return True, True
    if len(levelList) == 5:
        return False, False
    else:
        return len(levelList) - 1, levelList[len(levelList) - 1]


def SaveCharacter(player):
    """
    |    Save_Character:
    |    is the file-saving function.
    |    Using the pickle module, this function saves the object
    |    in bitstream within a pickle file under a .TOV extention
    """

    fileName = player.name + GetDateTime() + ".TOV"
    with open(fileName, "wb") as f:
        pickle.dump(player, f)


def GameLoadCharacter():
    """
    |    Load_Character:
    |    is the file-loading function.
    |    Using the pickle module this function loads
    |    character objects saved in bitstream.
    |    If no file is found the function returns False
    """

    ManageDir()

    if databank.loadNameList is None:
        print("There are no save files to load...")
        return False
    else:
        sentVar = True
        while sentVar:
            loadName = input("Please enter the name of your character\n"
                             "(type 'exit' when finished): ")
            if loadName.lower() == "exit":
                sentVar = False

            if not DuplicateCheck(loadName):
                print("There is no character saved under such name.. ")
                break
            else:
                print("Your character has been found..")
                loadFile = BackendLoadCharacter(loadName)
                return loadFile


def BackendLoadCharacter(name):
    """
    |   Backend_Load_Character:
    |   Function moves to saved_characters path
    |   then using the list from manage_dir, the 
    |   name needed within the file is parsed 
    |   then loaded. If no files are found func. returns false
    |   :param name: object(Player Class)  
    """
    dirPath = os.path.join(os.path.dirname(__file__), "Saved_Characters")

    loadList = os.listdir(dirPath)

    for path in loadList:
        if path.startswith(name):
            with open(path, "rb") as char_init:
                load_char = pickle.load(char_init)
                databank.characterLib = load_char
                return load_char

    return False


def StarLine(top = False):
    length = 60

    if not top:
        print("\n\n")

    count = 0
    while count < length:
        print("*", end = "")
        count += 1

    print("\n\n")


def QuitGame():
    return  sys.exit()

