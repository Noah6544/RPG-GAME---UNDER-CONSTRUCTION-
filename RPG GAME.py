#STARTED ON 12-12-19

#FILES

playerdata = open('playerdata.txt','r+')

#CLASSES
class Player: #todo finish this class and figure out it's funciton
    def __init__(self,attack,defense, speed, health):
        self.name = name

 #   def attack(self, attack, speed):
        #todo create an attack function that every class can use

class Warrior(Player):
    def __init__(self, attack, defense, speed, health):
        self.name = name
        self.attack = 150
        self.defense = 75
        self.speed = 25
        self.health = 105


class Knight(Player):
    def __init__(self, attack, defense, speed, health):
        self.name = name
        self.attack = 75
        self.defense = 150
        self.speed = 25
        self.health = 115


class Scout(Player):
    def __init__(self, attack, defense, speed, health):
        self.name = name
        self.attack = 75
        self.defense = 75
        self.speed = 100
        self.health = 110


###IMPORTS

import time
import random
from termcolor import colored, cprint

###VARIABLES

twenty = (colored("~~~~~~~~~~~~~~~~~~~~", 'yellow'))
twenty2 = (colored(twenty + "\n" + twenty, 'yellow'))
twentyalot = (colored(twenty + "\n" + twenty + "\n" + twenty + "\n" + twenty + "\n" + twenty))
yes = ("yes", "YES", "Yes", "yEs", "yeS", "YEs", "YeS", "YEs", "YeS", "YeS", "yES", "Y", "y")
no = ("no", "No", "NO", "nO", "N", "n")
twenty_long = (twenty + "~~~~~~~~~~")
invalid_input = ()


###FUNCTIONS
def encount(encount, enstat, stat):
    global factsencount
    if enstat > stat:
        encount + 1
    elif enstat == stat:
        encount + 0
    elif enstat < stat:
        encount - 1
    factsencount = 0
    factsencount = encount + factsencount


def comparing_2(attack, enattack, ATTACK):
    ATTACK = str(ATTACK)
    if enattack > attack:
        print(twenty)
        print(
            colored("THE ENEMY'S " + ATTACK + " IS GREATER THAN YOURS BY\n" + twenty + str(enattack - attack), 'blue'))
        print(twenty)
        time.sleep(2)
    elif enattack < attack:
        print(twenty)
        print(colored("YOUR " + ATTACK + " IS GREATER THAN THE ENEMY'S BY\n" + twenty + str(attack - enattack), 'blue'))
        print(twenty)
        time.sleep(2)
    elif enattack == attack:
        print(twenty)
        time.sleep(2)
        print(colored("YOUR + " + ATTACK + " STATS ARE EQUAL", 'blue'))


def enemy(enattack, endefense, enspeed, enhealth, enname, attack, defense, speed, health, name):
    global would_you
    def comparing_stats:
        print(twenty_long)
        print(colored("THE ENEMY THAT YOU WILL BE FACING IS:", 'blue'))
        print(twenty)
        print(enname)
        print(twenty)
        print(colored("LET'S COMPARE YOUR STATS WITH THEIRS.", 'blue'))
        print(twenty2)
        print(colored("WOULD YOU LIKE TO GET A SYNOPSIS OF THE ENEMY'S STATS - [1]", 'red'))
        print(twenty2)
        print("BROKEN - CHOOSE 2")
        print(twenty2)
        print(twenty)
        time.sleep(3)
        print(colored("OR - WOULD YOU LIKE TO HAVE A MORE IN DEPTH VIEW OF THE ENEMY'S STATS? - [2]", 'red'))
        print(twenty)
        would_you = int(input(colored("[1] OR [2]", 'red')))
        print(twenty)
        if would_you == 1:
            encount = 0
            print(encount(encount, enattack, attack))
            print(encount(factsencount, endefense, defense))
            print(encount(factsencount, enspeed, speed))
            print(encount(factsencount, enhealth, health))
            if encount == 1:
                print(colored("THIS WILL BE AN EASY FIGHT", 'blue'))
                print(twenty)
                time.sleep(2)
            elif encount == 2:
                print(colored("THIS WILL BE A TOUGH FIGHT", 'blue'))
                print(twenty)
                time.sleep(2)
            elif encount == 3:
                print(colored("THIS WILL BE A HARD FIGHT", 'blue'))
                print(twenty)
                time.sleep(2)
            elif encount == 4:
                print(colored("THIS WILL BE A NEAR IMPOSSIBLE FIGHT", 'blue'))
                print(twenty)
                time.sleep(2)
            else:
                print(twenty)
                print(colored("THIS FIGHT WILL BE UNFATHOMABLY EASY", 'blue'))
                print(twenty)
                time.sleep(2)
        elif would_you == 2: #todo, just change the following code so that i doesn't say "the enemy has, you have" and just compare the first thing
            print(twenty)
            print("WE WILL BE COMPARING ATTACKS.")
            time.sleep(1)
            print(twenty)
            print("THE ENEMY HAS AN ATTACK OF:\n")
            print(twenty)
            print(str(enattack))
            print(twenty)
            time.sleep(1)
            print("YOU HAVE AN ATTACK OF:\n")
            print(twenty)
            print(str(attack))
            time.sleep(1)
            print(comparing_2(attack, enattack, 'ATTACK'))
            print(comparing_2(defense, endefense, 'DEFENSE'))
            print(comparing_2(speed, enspeed, 'SPEED'))
            print(comparing_2(health, enhealth, 'HEALTH'))
            arguably = int(random.randint(0, 100))
            if arguably > 49:
                print(twenty)
                print("THE ENEMY'S NAME IS ALSO ARGUABLY BETTER THAN YOURS...")
            elif arguably <= 49:
                print(twenty)
                print("YOUR NAME IS ALSO ARGUABLY BETTER THAN YOUR ENEMY'S NAME...")
            print(twenty)
            time.sleep(2)


def get_name():
    global name
    print(twenty)
    print(colored("I'VE FORGOTTEN TO GET YOUR NAME, PLEASE TELL ME.", 'blue'))
    print(twenty)
    name = str(input(colored("ENTER YOUR NAME: ", 'red')))
    return(twenty)
    time.sleep(1)


def stat_choosing():
    global attack
    global defense
    global speed
    global health
    print(colored("PICKING RANDOM (ATTACK) STAT NOW...", 'blue'))
    time.sleep(1.5)
    for i in range(6):
        print("Picking....", + i)
        time.sleep(.3)
        attack = random.randint(0, 100)
    print(twenty)
    print(colored("YOUR ATTACK STAT IS: " + str(attack), 'blue'))
    print(twenty)
    time.sleep(2)
    print(colored("PICKING RANDOM (DEFENSE) STAT NOW...", 'blue'))
    time.sleep(1.5)
    for i in range(6):
        print("Picking...", i)
        time.sleep(.3)
        defense = random.randint(0, 100)
    print(twenty)
    print(colored("YOUR DEFENSE STAT IS: " + str(defense), 'blue'))
    print(twenty)
    time.sleep(2)
    print(colored("PICKING RANDOM (SPEED) STAT NOW...", 'blue'))
    time.sleep(1.5)
    for i in range(6):
        print("Picking...", i)
        time.sleep(.3)
        speed = random.randint(0, 100)
    print(twenty)
    print(colored("YOUR SPEED STAT IS: " + str(speed), 'blue'))
    print(twenty)
    time.sleep(2)
    print(colored("PICKING RANDOM (HEALTH) STAT NOW...", 'blue'))
    time.sleep(1.5)
    for i in range(6):
        print(colored("Picking...", i, 'blue'))
        time.sleep(.3)
        health = random.randint(0, 25) + 100
    print(twenty)
    print(colored("YOUR HEALTH STAT IS: " + str(health), 'blue'))
    print(twenty2)


def class_choosing():
    global player
    global choose_class
    global do_you
    bool = True
    while bool == True:
        print(twenty)
        do_you = int(
            input(colored("DO YOU WANT TO PICK YOU CLASS - [1]\nOR RECIEVE A RANDOM CLASS [2]?\n" + twenty, 'red')))
        time.sleep(.5)
        if do_you == 1:
            print(twenty)
            print(colored("YOU WILL BE PICKING A CLASS\nPICK ONE OF THE FOLLOWING:", 'blue'))
            print(twenty)
            time.sleep(1)
            print(colored("1.WARRIOR\n-ATTACK: 150\n-DEFENSE: 75\n-SPEED: 25\n-HEALTH: 105", 'blue'))
            print(twenty)
            time.sleep(1)
            print(colored("2.KNIGHT\n-ATTACK: 75\n-DEFENSE: 150\n-SPEED: 25\n-HEALTH: 115", 'blue'))
            print(twenty)
            time.sleep(1)
            print(colored("3.SCOUT\n-ATTACK: 75\n-DEFENSE: 100\n-SPEED: 75\n-HEALTH: 110", 'blue'))
            print(twenty)
            time.sleep(2)
            choose_class = int(input(colored("WHICH CLASS WOULD YOU LIKE TO CHOOSE?", "red")))
            try:
                if choose_class == 1:
                    time.sleep(2)
                    print(twenty)
                    print(colored("YOU CHOSE THE WARRIOR CLASS.", 'blue'))
                    print(twenty)
                    time.sleep(1)
                    player = Warrior(150, 75, 25, 105, name)
                    bool = False
                elif choose_class == 2:
                    time.sleep(2)
                    print(twenty)
                    print(colored("YOU CHOSE THE KNIGHT CLASS.", 'blue'))
                    print(twenty)
                    time.sleep(1)
                    player = Knight(75, 150, 25, 115, name)
                    bool = False
                elif choose_class == 3:
                    time.sleep(2)
                    print(twenty)
                    print(colored("YOU CHOSE THE SCOUT CLASS.", 'blue'))
                    print(twenty)
                    time.sleep(1)
                    player = Scout(75, 100, 75, 110, name)
                    bool = False
            except:
                print(twenty)
                print(colored("INVALID INPUT\nMUST BE \'1 - 3\'\nPLEASE TRY AGAIN"))
                print(twenty)
        elif do_you == 2:
            print(twenty)
            print(colored("YOU WILL BE REC-IVING A RANDOM CLASS", 'blue'))
            print(stat_choosing())
            bool = False
        else:
            print(twenty)
            print(colored("INVALID INPUT, TRY AGAIN.", 'green'))
            print(twenty2)


###RUNNING

print(colored("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 'yellow'))
intro_have_you = str(input(colored("Have you played this before?\n[YES][NO]", 'red'))) #todo, this might be tough but just make another branch. rn. i will. make it so that the information saves to a file and that the play can access it next time
#converts intro_have_you to a boolean. True for yes, False for no.
if intro_have_you in yes:
    intro_have_you_bool = True
elif intro_have_you in no:
    intro_have_you_bool = False
playerdata.write(str(intro_have_you_bool))

if intro_have_you_bool == True:
    get_name()
    print(class_choosing())
elif intro_have_you_bool == False:
    print(get_name())
    print(twenty)
    print(colored(
        "THIS IS AN RPG GAME - THE GOAL IS TO GET AS FAR AS POSSIBLE.\nYOU WILL BE PROMPTED TO EITHER CHOOSE OR MAKE YOUR CLASS, IF YOU CHOOSE MAKE CLASS[BROKEN], THEN YOU'LL HAVE A MAX OF 250 POINTS TO DISTRIBUTE TO ALL YOUR STATS - YOUR HEALTH STAT SIMPLY ADDS THAT MUCH HEALTH TO YOUR BASE HEALTH OF 100",
        'blue'))
    time.sleep(1.5)
    print(twenty)
    print(class_choosing())

if do_you == 1:
    print(colored("THIS MEANS YOUR STATS ARE: \n1.ATTACK: " + str(player.attack) + "\n2.DEFENSE: " + str(
        player.defense) + "\n3.SPEED: " + str(player.speed) + "\n4.HEALTH:" + str(player.health), 'blue'))
    time.sleep(3)
elif do_you == 2:
    print(colored(
        "THIS MEANS YOUR STATS ARE: \n1.ATTACK: " + str(attack) + "\n2.DEFENSE: " + str(defense) + "\n3.SPEED: " + str(
            speed) + "\n4.HEALTH:" + str(health), 'blue'))
    time.sleep(3)
    print(twenty)
    print(colored("NOW THAT YOU HAVE YOUR STATS, YOU CAN START PLAYING.", 'blue'))
    time.sleep(2)
print(twenty2)
print(colored("PART 1 - TRAPPED ", 'green'))
print(twenty2)
time.sleep(1)
print(colored("YOU WILL FACE YOUR FIRST ENEMY, AND, I SHOULD WARN YOU. HE'S QUITE STONG.", 'blue'))
print(twenty)
time.sleep(3)
if do_you == 1:
    print(enemy(400, 400, 12, 12, 'SIMA', player.attack, player.defense, player.speed, player.health, player.name))
elif do_you == 2:
    print(enemy(400, 400, 12, 12, 'SIMA', attack, defense, speed, health, name))
    print("1")

###PAST BROKEN STUFF - MOVE ON MAYBE

"""
    (line 95)
    ###OPTION 1 BROKEN - FIX THIS
    if do_you == 1:  
      print(twenty2)
      print(colored("YOU WILL BE PICKING YOUR STATS", 'blue'))
      print(twenty)
      time.sleep(1.5)
      remaining_points = 250
      while (remaining_points - attack) < 0:
        attack = int(input(colored("WHAT WOULD YOU LIKE YOUR ATTACK STAT TO BE?(MAX 250 FOR ALL STATS(attack, speed, and defense)", 'red')))
        if (remaining_points - attack) >= 0:
          break
        elif remaining_points - attack < 0:
          time.sleep(2)
          print(twenty)
          print(colored("INVALID INPUT", 'green'))
          time.sleep(2)
      while remaining_points - defense > 0:
          remaining_points =remaining_points - attack
          print(twenty)
          print(colored("YOU HAVE " + str(remaining_points) + " POINTS REMAINING", 'blue'))
          time.sleep(2)
          print(twenty)
          defense = int(input(colored("WHAT WOULD YOU LIKE YOUR DEFENSE STAT TO BE? YOU HAVE " + str(remaining_points) + " POINTS REMAINING.",'red')))
      remaining_points = remaining_points - defense
      time.sleep(2)
      print(twenty)
      print(colored("YOU HAVE " + str(remaining_points) + " POINTS REMAINING", 'blue'))
      print(twenty)
      time.sleep(2)
      speed = int(input(colored("WHAT WOULD YOU LIKE YOUR SPEED STAT TO BE? YOU HAVE " + str(remaining_points) + " POINTS REMAINING.",'red')))
      print(twenty)
      time.sleep(2)
    """
