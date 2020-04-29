import time
import random

items_in_bag = []
list_of_monsters = ["Troll" ,"Dragons" ,"Pirates" ,"Ninja" ]
chosen_monster = random.choice(list_of_monsters)

def print_with_pause(to_be_printed):
    print(to_be_printed)
    #time.sleep(2)

def intro():
    print_with_pause("You find yourself in an open field, filled with grass yellow wildflowers.")
    print_with_pause("Rumor has it that a pirate is somewhere around here, and has been terrifying the nearby village.")
    print_with_pause("In front of you is a house.")
    print_with_pause("To your right is a dark cave.")
    print_with_pause("In your hand you hold your trusty (but not very effective) dagger.")

def option():
    print_with_pause("\nEnter 1 to knock on the door of the house")
    print_with_pause("Enter 2 to peer into the cave")
    print_with_pause("What would you like to chose?")
    while True:
        answer=input("(Please enter 1 or 2)")
        if answer == "1":
            house()
            break
        elif answer == "2":
            cave()
            break
        else:
            continue

def cave():
    print_with_pause("You peer cautiously into the cave.")
    if "sword" in items_in_bag:
        print_with_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")

    else: and "sword" in items_in_bag
        items_in_bag.append("sword")
        print_with_pause("It turns out to be only a very small cave.")
        print_with_pause("Your eyes catches a glint of metal behind a rock.")
        print_with_pause("You found the magical sword of Ogoroth.")
        print_with_pause("You discard your silly little dagger and take the sword with you.")

    print_with_pause("You walk back out to the field.")
    option()


def house():
    print_with_pause("You approach the door of the house.")
    print_with_pause("You are about knock when the door opens and steps out a " + chosen_monster)
    print_with_pause("Eep! This is the " + chosen_monster +"'s house!")
    print_with_pause("The pirate attacks you.")
    if "sword" not in items_in_bag:
        print_with_pause("You feel a bit under-prepared for this, what with having only a tiny dagger.")
    fight()

def fight():
    while True:
        value = input("Would you like to (1)Fight or (2)run away?")
        if value == "1" and  "sword" in items_in_bag:
            print_with_pause("As the " +chosen_monster +" moves to attack, you unsealth your sword.")
            print_with_pause("The sword of Ozoroth shines brightly in your hand as you brace yourself for the attack.")
            print_with_pause("But the " + chosen_monster + " takes a look at your shiny new toy and runs away.")
            print_with_pause("You have ridden the town of the " + chosen_monster + ".You are victorious.")
            break
        elif value == "1" and "sword" not in items_in_bag:
            print_with_pause("You do your best..")
            print_with_pause("but your danger is no match for the "+chosen_monster)
            print_with_pause("You've been defeated.")
            break
        elif value == "2":
            print_with_pause("You run back into the field. Luckily you don't seem to have been followed.")
            option()
        else:
            continue

def main():
    intro()
    option()
    while True:
        play_again = input("Would you like to play again?(y/n)")
        if play_again == 'y':
            print_with_pause("Excellent! Restarting the game..")
            intro()
            option()
        elif play_again == 'n':
