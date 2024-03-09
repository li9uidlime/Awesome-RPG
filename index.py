import random, os, json
from time import sleep
os.system("title Awesome RPG - Made by TAEIN")
def clear():
  os.system("cls")
import sys
import time
def twp(text, seep):
  for char in text.center(100, " "):
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(seep)
  print()
from IPython.display import HTML

colormap = {
  "red": "\033[31m",
  "green": "\033[32m",
  "yellow": "\033[33m",
  "blue": "\033[34m",
  "magenta": "\033[35m",
  "cyan": "\033[36m",
  "white": "\033[37m"
}

def ColorPrint(text, color):
    print((colormap[color]+text+"\033[0m").center(100, " "))

class Screen():
    def main():
        clear()
        print("[ ########### ]".center(100," "))
        print("| Awesome RPG |".center(100," "))
        print("[ ########### ]".center(100," "))
        print()
        print("1) Game Start".center(100," "))
        print("2) Exit".center(100," "))
        print()
        choice = input("> ")
        if choice == "1":
            sleep(0.5)
            clear()
            print("Loading world data... (0/2)".center(100," "))
            with open ("WorldData.json", "r") as f:
                WorldData = json.load(f)
            sleep(0.5)
            clear()
            print("Loading player data... (1/2)".center(100," "))
            with open ("PlayerData.json", "r") as f:
                PlayerData = json.load(f)
            sleep(0.5)
            clear()
            print("Done! (2/2)".center(100," "))
            sleep(1)
            Game.GreenLeaf()
        elif choice == "2":
            clear()
            exit()
        else:
            Screen.main()
class Game():
    def GreenLeaf():
        clear()
        ColorPrint("~ Greenleaf ~", "green")
        twp("\033[36m「A peaceful village surrounded by green forests」", 0.05)
        twp("\033[35m( Press Enter to enter Greenleaf )", 0.05)
        input("\033[0m")
        while True:
            clear()
            print("\033[32m~ Greenleaf ~\033[33m".center(100, " "))
            print("\n1) Dungeon\n2) Shop\n3) Equipment Enhancement\n4) Inventory")
            choice = input("\033[0m> ")
            if choice == "1":
                clear()
                ColorPrint("~ Dungeons ~", "red")
                print()
                ColorPrint("0) Back to GreenLeaf", "white")
                ColorPrint("1) Polluted forest ★☆☆", "green")
                ColorPrint("2) The Bandit's Hideout ★★☆", "yellow")
                ColorPrint("3) Forgotten castle ★★★", "red")
                choice = input("> ")
                if choice == "0":
                    pass
                elif choice == "1":
                    pass
            


class Dungeon():
    def PollutedForest():
        clear()
Screen.main()