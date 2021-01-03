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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

mountain = input("You've come to a mountain do you want to climb over it or go around it? Type 'climb' or 'around' \n")

mountain_lwr = mountain.lower()

if mountain_lwr == "around":
  lake = input("You come to a lake.  There is an island in the middle of the lake.  Type 'wait' to wait for the boat. Type 'swim' to awim to the island. \n").lower()
  if lake == "wait":
    door = input("Way to go! you've made it to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.  Which colour do you choose? \n").lower()
    if door == "red":
      print("You entered the dragons den! Game Over :(")
    elif door == "yellow":
      print("You walked into poisonous fog! Game Over :(")
    elif door == "blue":
      print("Congratulations! You found the treasure! You win!")
    else:
      print("Sorry, that door does not exist. Game Over :(")
  else:
    print("You drowned! Game Over :(")
else:
  print("You fell! Game Over :(")
