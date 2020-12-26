import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, your choice was not recognised.")
    return response


def intro(character):
    print_pause('You find yourself standing in an open field, \
filled with grass and yellow wildflowers.')
    print_pause('Rumor has it that a ' + (character) + ' is somewhere \
around here, and has been terrifying the nearby village.')
    print_pause("In front of you is a house.\nTo your right is a dark cave.\n\
In your hand you hold your trusty (but not very effective) dagger.")


def user_choice(weapons_cache, character):
    user_choice_direction = valid_input("Enter 1 to knock on the door of the \
house.\nEnter 2 to peer into the cave. What would you like to do? \n\
(Please enter 1 or 2.)",  "1", "2")
    if "1" in user_choice_direction:
        go_house(weapons_cache, character)
    elif "2" in user_choice_direction:
        go_cave(weapons_cache, character)


def go_cave(weapons_cache, character):
    if "sword" not in weapons_cache:
        print_pause("You peer cautiously into the cave. \nIt turns out\
to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock. \n\
You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword\
with you. \nYou walk back out to the field.")
        weapons_cache.append("sword")
        user_choice(weapons_cache, character)
    else:
        print_pause("You peer cautiously into the cave.\n You've been here\
 before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        user_choice(weapons_cache, character)


def go_field(weapons_cache, character):
    print_pause("You run back into the field. Luckily, you don't seem\
 to have been followed.")
    user_choice(weapons_cache, character)


def go_fight(weapons_cache, character):
    if "sword" in weapons_cache:
        print_pause("As the  " + (character) + " moves to attack,\
you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand\
as you brace yourself for the attack.")
        print_pause("But the " + (character) + " takes one look at your \
shiny new toy and runs away!")
        print_pause("You have rid the town of the " + (character) + "\
 You are victorious!")
        play_again()
    else:
        print_pause("You feel a bit under-prepared for this, what with\
 only having a tiny dagger.")
        fight_time = valid_input("Would you like to (1) fight or (2)\
run away?", "1", "2")
        if "1" in fight_time:
            print_pause("You do your best... \n but your dagger is no \
match for the " + character + ".")
            print_pause("You have been defeated!")
            play_again()
        elif "2" in fight_time:
            go_field(weapons_cache, character)


def go_house(weapons_cache, character):
    print_pause("You are about to knock when the door opens and out\
steps a " + (character))
    print_pause("Eep! This is the " + (character) + "'s house!\n\
The " + (character) + " attacks you!")
    user_fight_choice = valid_input("""Would you like to (1) fight or
(2) run away?""", "1", "2")
    if "1" in user_fight_choice:
        go_fight(weapons_cache, character)
    elif "2" in user_fight_choice:
        go_field(weapons_cache, character)


def play_again():
    play_again_choice = valid_input("Would you like to play again?\
(y/n)", "y", "n")
    if "y" in play_again_choice:
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif "n" in play_again_choice:
        print_pause("Thanks for playing! See you next time.")


def play_game():
    character = random.choice(["dragon", "fairie", "pirate"])
    weapons_cache = []
    intro(character)
    user_choice(weapons_cache, character)


play_game()
