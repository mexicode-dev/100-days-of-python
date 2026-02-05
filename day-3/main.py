print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')


print("Welcome to Treasure Island.")
print("Your mission: find the hidden treasure before sunset.")
      
cross_road = input('''You're at a dusty crossroad. The wind whispers through dead trees.
\tType "left" or "right"\n ''').lower()

if cross_road == "left":
    lake_area = input('''You reach a silent lake. Fog crawls over the water.\nAn island sits in the middle like a shadow.\nType "wait" for a boat or "swim" to cross.\n''').lower()
    if lake_area == "wait":
        door_area = input('''A small boat arrives without a sound.\nYou reach the island and find three ancient doors:\n"red", "blue", or "yellow". Which one do you open?\n''').lower()
        if door_area == "yellow":
            print('''The yellow door creaks open…\nA warm golden light floods the room.\nYou found the treasure. You win! 🏆''')
        else:
            print("The door slams shut behind you.\nA curse awakens in the dark.\nGame Over!")
    else:
        print("You dive in. The water is freezing… and something pulls your ankle.\nGame Over!")
elif cross_road == "right":
    print("You take the right path. The ground cracks beneath you—\na concealed pit opens.\nGame Over. Try again!")
else:
    print('''Confused, you wander in circles until night falls.\nType exactly: "left" or "right".''')