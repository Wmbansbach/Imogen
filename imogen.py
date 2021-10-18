#! python3.py 
__author__ = "WmBansbach"
""" IMOGEN_JAN2018_VS - Text Based Role-Playing Game
    
    Main Entry-Point of game
"""

import sys
import start_menu
import manager


if __name__ == "__main__":

    game_over = False

    while not game_over:
       
        start_menu.startMenu()
        manager.Manager()

    sys.exit()



