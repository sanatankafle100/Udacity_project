import time
import random

items_in_bag = []
list_of_monsters = ["Troll", "Dragons", "Pirates", "Ninja"]
chosen_monster = random.choice(list_of_monsters)


def print_with_pause(to_be_printed, sleep_time):
    print(to_be_printed)
    time.sleep(sleep_time)


def intro():
    print_with_pause("You find yourself in an open field"
                     "filled with grass yellow wildflowers.", 2)
    print_with_pause("Rumor has it that a pirate is somewhere around here,"
                     "and has been terrifying the nearby village.", 2)
    print_with_pause("In front of you is a house.", 1)
    print_with_pause("To your right is a dark cave.", 1)
    print_with_pause("In your hand you hold your trusty"
                     "(but not very effective) dagger.", 2)


def option():
    print_with_pause("\nEnter 1 to knock on the door of the house", 1)
    print_with_pause("Enter 2 to peer into the cave", 1)
    print_with_pause("What would you like to chose?", 1)
    while True:
        answer = input("(Please enter 1 or 2)",)
        if answer == "1":
            house()
            break
        elif answer == "2":
            cave()
            break
        else:
            continue


def cave():
    print_with_pause("You peer cautiously into the cave.", 1)
    if "sword" in items_in_bag:
        print_with_pause("You've been here before, and gotten all"
                         "the good stuff. It's just an empty cave now.", 2)

    else:
        items_in_bag.append("sword")
        print_with_pause("It turns out to be only a very small cave.", 1)
        print_with_pause("Your eyes catches a glint of metal behind a rock.",
                         1)
        print_with_pause("You found the magical sword of Ogoroth.", 1)
        print_with_pause("You discard your silly little dagger"
                         "and take the sword with you.", 2)

    print_with_pause("You walk back out to the field.", 1)
    option()


def house():
    print_with_pause("You approach the door of the house.", 1)
    print_with_pause("You are about knock when the door opens and"
                     "steps out a " + chosen_monster, 1)
    print_with_pause("Eep! This is the " + chosen_monster + "'s house!", 1)
    print_with_pause("The pirate attacks you.", 1)
    if "sword" not in items_in_bag:
        print_with_pause("You feel a bit under-prepared for this,"
                         "what with having only a tiny dagger.", 2)
    fight()


def fight():
    while True:
        value = input("Would you like to (1)Fight or (2)run away?")
        if value == "1" and "sword" in items_in_bag:
            print_with_pause("As the " + chosen_monster + " move"
                             "to attack, you unsealth your sword.", 2)
            print_with_pause("The sword of Ozoroth shines brightly in your"
                             "hand as you brace yourself for the attack.", 2)
            print_with_pause("But the " + chosen_monster + " takes a"
                             "look at your shiny new toy and runs away.", 2)
            print_with_pause("You have ridden the town of the " +
                             chosen_monster + ".You are victorious.", 2)
            break
        elif value == "1" and "sword" not in items_in_bag:
            print_with_pause("You do your best..", 1)
            print_with_pause("but your danger is no match for the " +
                             chosen_monster, 1)
            print_with_pause("You've been defeated.", 1)
            break
        elif value == "2":
            print_with_pause("You run back into the field. Luckily "
                             "you don't seem to have been followed.", 2)
            option()
            break
        else:
            continue


def main():
    intro()
    option()
    while True:
        play_again = input("Would you like to play again?(y/n)")
        if play_again.lower() == 'y':
            items_in_bag = []
            print_with_pause("Excellent! Restarting the game..", 1)
            intro()
            option()
        elif play_again.lower() == 'n':
            print_with_pause("Thanks for playing. See you next time.", 1)
            break


main()
