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

left_or_right = input("You are at the cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if left_or_right == "left":
  swim_or_wait = input("You\'ve come to a lake and see an island in the middle of it. Do you want to swim or wait? Type 'swim' to swim across. Type 'wait' to wait for a boat.\n").lower()
  if swim_or_wait == "wait":
    choose_door = input("You've made it to the island safely. There is a castle with three doors. One is red, yellow and blue. Which door do you choose?\n").lower()
    if choose_door == "yellow":
      print("You've found a treasure! Congrats!")
    elif choose_door == "red":
      print("You stepped on a mine and got blown up. Game over.")
    elif choose_door == "blue":
      print("You've been obducted by alians. Game over.")
    else:
      print("Game over.")
  else:
    print("Did you forget you can't swim? You drowned. Game over.")   
else:
  print("You ran into a bear and became a snack. Game over.")
  
