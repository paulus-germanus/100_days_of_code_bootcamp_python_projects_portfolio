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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("You're at a crossroad. Would you like to go left or right?\n").lower()
if left_right == "left":
    swim_wait = input("You've come to a lake with an island in the middle of it. Would you like to swim or wait? \n").lower()
    if swim_wait == "wait":
        door = input("For some reason waiting alone somehow got you transported to the island and you've found a house "
                     "with 3 doors. Which door do you choose? Red, blue or yellow?\n").lower()
        if door == "red":
            print("You've got your bum immolated to fine ash by infernal flames.\nGame Over.")
        elif door == "blue":
            print("You've got your sorry rear eaten by feral beasts of the night.\nGame Over.")
        elif door == "yellow":
            print("(by pure chance and coincidence...)\nYou Win!")
        else:
            print("There ain't no such doar, brova®. Play again.")
    else:
        print("All of a sudden you got attacked by the biggest trout in the known universe.\nGame Over.")
else:
    print("You well into a hole.\nGame Over.")
