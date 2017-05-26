import random
import os
import sys

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
        
def user_choice():
    return input("> ").lower().strip()

def wait():
    if INTERACTIVE_MODE:
        input("Press enter to continue.")
        
def space_count2():
    print("-----\n"
          "|    |\n"
          "-----\n")
    print("-----\n"
          "|    |\n"
          "-----\n")
    print("How many asteroids are there?")
    choice = user_choice()
    if choice == "2":
        print("Correct!")
        print("More comming soon!")
        wait()
        menu()

def space_count():
    clear_screen()
    print("-----\n"
          "|   |\n"
          "-----")
    print("How many asteroids are there?")
    choice = user_choice()
    if choice == "1":
        print("Correct!")
        clear_screen()
        space_count2()

def menu():
    clear_screen()
    print("================\n"
          "~~~Multi~Game~~~\n"
          "================\n")
    print("1. Space Game")
    choice = user_choice()
    if choice == "1":
        space_count()

menu = menu()
print(menu)
